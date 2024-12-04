
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import requests
import json
import argparse # to handle command-line arguments in Python 

##### Configuration
# to create an api_key visit: https://fwksimulationlogger.fz-rossendorf.de/login
# to login enter the username and password.
# After login click on ** View Account/Generate API Token** at the top menu of the website. Then, generate an API Token (api_key).
#create an api_key.txt and copy the api_key value.


# Create an argument parser
parser = argparse.ArgumentParser(description='Process input for file transfer.')

# Add expected arguments
parser.add_argument('--api_key_file', required=True, help='Path to the API key file')
parser.add_argument('--upload_type', default='PIConGPU_cwtool', help='Upload type')
parser.add_argument('--username', default='afshar87', help='Username')
parser.add_argument('--directory_path', required=True, help='Directory path containing the JSON file')
parser.add_argument('--json_file_name', default='pypicongpu.json', help='Name of the JSON file')
parser.add_argument('--description', required=True, help='Description for the upload')
parser.add_argument('--keywords', nargs='+', help='Keywords for the upload')
args = parser.parse_args()

# Access the arguments
api_key_file = args.api_key_file
upload_type = args.upload_type
username = args.username
directory_path = args.directory_path
json_file_name = args.json_file_name
description = args.description
keywords = args.keywords



BASE_URL = 'fwksimulationlogger.fz-rossendorf.de'
api_url = 'https://{}/api/upload'.format(BASE_URL)

path_to_data = os.path.join(directory_path, json_file_name)
print("Path to data: {}".format(path_to_data))

# Read the API key from the text file
with open(api_key_file, 'r') as file:
    api_key = file.read().strip()                        # Read and remove any extra whitespace or newline characters

# Now you can use api_key in your code
# print("API key: {}".format(api_key))

# install required packages
def install_package(package_name):
    """Install the specified package using pip."""

    print("Installing {} using {}...".format(package_name, sys.executable))
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print("{} installed successfully.".format(package_name))
    except subprocess.CalledProcessError as e:
        print("Failed to install {}: {}".format(package_name, e))
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



### for debugging: List files in the directory for debugging
# print("Listing files in directory:", directory_path)
# for filename in os.listdir(directory_path):
#     print(filename)

# Verify the file exists
if not os.path.isfile(path_to_data):
    raise IOError("The file at {} does not exist.".format(path_to_data))

# Prepare the data and file for the request
data = {
    'upload_type': upload_type,
    'path_to_data': path_to_data,
    'description': description,
    'keywords': ','.join(keywords),
    'username': username  # Add username here
}

files = {
    'metadataFile': open(path_to_data, 'rb')  # Assuming 'metadataFile' is the correct key
}

# Prepare headers
headers = {
    'Authorization': 'Bearer {}'.format(api_key)  # Use 'Bearer' if that’s the expected scheme
}

# Perform the file upload
try:
    response = requests.post(api_url, headers=headers, data=data, files=files)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    print("File uploaded successfully!")
except requests.exceptions.HTTPError as err:
    print("Failed to upload file. Status code: {}".format(response.status_code))
    print("Response: {}".format(response.text))
except Exception as e:
    print("An error occurred: {}".format(str(e)))
finally:
    files['metadataFile'].close()  # Close the file when done
