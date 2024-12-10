##### how to create an api_key 
# visit: https://fwksimulationlogger.fz-rossendorf.de/login
# to login enter the username and password.
# After login click on ** View Account/Generate API Token** at the top menu of the website. Then, generate an API Token (api_key).
#create an api_key.txt and copy the api_key value.


import sys
# print("Python executable:", sys.executable)
# print("Python version:", sys.version)
# print("Python path:", sys.path)
sys.path.append('/home/afshar87/.local/lib/python3.6/site-packages')

import argparse # to handle command-line arguments in Python 
import subprocess
import os
import json
# -*- coding: utf-8 -*-

# install required packages
def install_package(package_name):
    """Install the specified package using pip."""
    print(f"Installing {package_name} using {sys.executable}...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', package_name])
        print(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")
    except Exception as e:
        print(f"Unexpected error during installation: {e}")


def main():
    """Check and install the requests package."""
    try:
        import requests
        print("requests is already installed.")
    except ImportError:
        print("requests not found. Installing...")
        install_package('requests')
        # Try to import again after installation
        if 'requests' not in sys.modules:
            import requests
            print("requests installed and imported successfully.")
            
if __name__ == "__main__":
    main()


# IMPORTANT: since some required packages are not installed by default (eg requests), first we should install them hence import section comes after packages installations.

import requests

# Create an argument parser
parser = argparse.ArgumentParser(description='Process input for file transfer. Upload files to an API.')

# Add expected arguments
parser.add_argument('--json_file_path', required=True, help='Full path to the JSON file')
parser.add_argument('--api_key_file', required=True, help='Path to the API key file')
parser.add_argument('--upload_type', default='PIConGPU', help='Upload type')
parser.add_argument('--username', default='afshar87', help='Username')
parser.add_argument('--description', required=True, help='Description for the upload')
parser.add_argument('--keywords', nargs='+', help='Keywords for the upload')
parser.add_argument('--file_paths', nargs='+', required=True, help='List of file paths to upload')

args = parser.parse_args()

# Access the arguments
json_file_path = args.json_file_path
api_key_file = args.api_key_file
upload_type = args.upload_type
username = args.username # don't technically need username since you're using api_key which is linked to user
description = args.description
keywords = args.keywords
file_paths = args.file_paths

# # Debug: Output raw file paths
# print(f"Raw file_paths from args: {file_paths}")
# print(f"Type of file_paths: {type(file_paths)}")

# Ensure file_paths is a list of strings
# if not isinstance(file_paths, list) or not all(isinstance(fp, str) for fp in file_paths):
#     raise TypeError(f"file_paths must be a list of strings. Got: {file_paths}")

# Group important metadata into a dictionary
metadata = {
    'upload_type': upload_type,
    'description': description,
    'keywords': ','.join(keywords) if keywords else '',
}


BASE_URL = 'fwksimulationlogger.fz-rossendorf.de'
api_url = 'https://{}/api/upload'.format(BASE_URL)

# Read the API key from the file
with open(api_key_file, 'r') as file:
    api_key = file.read().strip()
    
    
# Prepare the headers
headers = {
    'Authorization': f'Bearer {api_key}',  # Correct format for Bearer token
}

# Initialize variables for file processing
total_size = 0
open_files = []  # To keep track of open file handles
processed_files = []  # To store file data for the 'processedDataFiles' field

if file_paths:
    # Iterate over each file path
    for file_path in file_paths:
        file_path = file_path.strip()  # Remove leading/trailing whitespace
        
        if os.path.exists(file_path):
            print(f"Processing file: {file_path}")

            try:
                # Open the file in binary mode
                file = open(file_path, 'rb')
                # Add to processed files as a tuple (file_name, file_handle, mime_type)
                processed_files.append(('processedDataFiles', (os.path.basename(file_path), file, 'application/octet-stream')))
                open_files.append(file)  # Keep track of open files

                # Calculate the total size of files
                file.seek(0, 2)  # Move to the end of the file to get its size
                total_size += file.tell()
                file.seek(0)  # Reset the file pointer to the beginning

                # Check if the total size exceeds 1GB
                if total_size > 1 * 1024 * 1024 * 1024:  # 1GB limit
                    print('Total file size exceeds 1GB. Please reduce the file sizes.')
                    sys.exit()
            except Exception as e:
                print(f"Error opening file {file_path}: {e}")
                sys.exit()
        else:
            print(f"File {file_path} does not exist.")
            sys.exit()

    # Prepare the files dictionary for the POST request
    files = {
        'metadataFile': ('metadata.json', open(json_file_path, 'rb'), 'application/json'),
    }

    # Append all processed files (including the ones added to 'processedDataFiles') to files
    files.update(dict(processed_files))

    # Debug: Print processed files for verification
    print(f"Processed files: {processed_files}")
    
    # Make the API request with metadata as json
    try:
        response = requests.post(api_url, headers=headers,  data=(metadata), files=files)  # 
        response.raise_for_status()  # Raise HTTPError for bad responses
        print("Files uploaded successfully!")
        print("Response:", response.text)
    except requests.exceptions.HTTPError as err:
        print(f"Failed to upload files. Status code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close all opened file objects
        for file in open_files:
            file.close()
else:
    print("No files specified in file_paths.")
    sys.exit()