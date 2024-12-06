import os
import subprocess
import sys

# Function to check if the repo is cloned
def check_and_clone_repo(picmi_git_path, picmi_local_dir, picmi_input_json):
    print(f"Current working directory: {os.getcwd()}")  # Log the current working directory
    if not os.path.isdir(picmi_local_dir):
        print(f"Cloning PICMI repository from {picmi_git_path} into {picmi_local_dir}...")
        subprocess.run(['git', 'clone', picmi_git_path, picmi_local_dir], stdout=open(picmi_input_json, 'w'), stderr=subprocess.STDOUT)
    else:
        print(f"PICMI repository already exists in {picmi_local_dir}. Checking for updates...")
        os.chdir(picmi_local_dir)
        subprocess.run(['git', 'fetch', 'origin'], stdout=open(picmi_input_json, 'w'), stderr=subprocess.STDOUT)
        default_branch = subprocess.check_output(
            ["git", "remote", "show", "origin"],
            universal_newlines=True
        ).splitlines()
        
        # Find default branch name
        for line in default_branch:
            if "HEAD branch" in line:
                default_branch_name = line.split(":")[1].strip()
                break
        else:
            print("Unable to determine the default branch. Exiting...")
            return
        
        print(f"Pulling the latest changes from the {default_branch_name} branch...")
        subprocess.run(['git', 'pull', 'origin', default_branch_name], stdout=open(picmi_input_json, 'w'), stderr=subprocess.STDOUT)

# Main function
def main():
    if len(sys.argv) != 4:
        print("Error: Please provide the git URL, repo directory, and log file path.")
        sys.exit(1)

    picmi_git_path = sys.argv[1]  # Get the git URL from command-line argument
    picmi_local_dir = sys.argv[2]  # Get the repo directory from command-line argument
    picmi_input_json = sys.argv[3]  # Get the log file path from command-line argument

    check_and_clone_repo(picmi_git_path, picmi_local_dir, picmi_input_json)

if __name__ == '__main__':
    main()
