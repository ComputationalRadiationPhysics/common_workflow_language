import os
import shutil
import sys

def update_profile(profile_name, new_my_mail, new_my_mailnotify, picsrc, tbg_partition, simulation_output_path):
    # Define the profile file's source path
    profile_src = os.path.join(picsrc, "etc", "picongpu", "hemera-hzdr", f"{profile_name}.example")
    
    # Create the profile directory if it doesn't exist
    profile_dir = "profile"  # Directory where the profile will be stored
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)

    # Define the destination profile path
    profile_dest = os.path.join(profile_dir, profile_name)
    
    # Copy the profile from source to destination using shutil.copy
    if os.path.exists(profile_src):
        shutil.copy(profile_src, profile_dest)
    else:
        print(f"Error: {profile_src} does not exist.")
        sys.exit(1)

    # Read the profile file to modify it
    with open(profile_dest, 'r') as file:
        profile_content = file.read()

    # Perform replacements for each parameter
    profile_content = profile_content.replace('export MY_MAILNOTIFY="NONE"', f'export MY_MAILNOTIFY="{new_my_mailnotify}"')
    profile_content = profile_content.replace('export MY_MAIL="someone@example.com"', f'export MY_MAIL="{new_my_mail}"')
    # profile_content = profile_content.replace('export PICSRC=.*', f'export PICSRC={picsrc}')
    profile_content = profile_content.replace('export TBG_partition="fwkt_v100"', f'export TBG_partition="{tbg_partition}"')
    import re
    # Match and replace PICSRC using a regex pattern
    profile_content = re.sub(r'export PICSRC=.*', f'export PICSRC={picsrc}', profile_content)

    # Append the SCRATCH variable to the file
    profile_content += f'\nexport SCRATCH={simulation_output_path}\n'

    # Print the updated profile content to stdout
    print("\n#Updated profile content:\n")
    print(profile_content)

    # Write the updated content back to the profile file
    with open(profile_dest, 'w') as file:
        file.write(profile_content)

    #print(f"Profile file updated successfully: {profile_dest}")

def main():
    # Parse arguments passed by CWL
    if len(sys.argv) != 7:
        print("Usage: python3 3-1-update_profile.py <profile_name> <new_my_mail> <new_my_mailnotify> <picsrc> <tbg_partition> <simulation_output_path>")
        sys.exit(1)

    # Map positional arguments to variables
    profile_name = sys.argv[1]
    new_my_mail = sys.argv[2]
    new_my_mailnotify = sys.argv[3]
    picsrc = sys.argv[4]
    tbg_partition = sys.argv[5]
    simulation_output_path = sys.argv[6]

    # Call the function to update the profile
    update_profile(profile_name, new_my_mail, new_my_mailnotify, picsrc, tbg_partition, simulation_output_path)

if __name__ == '__main__':
    main()
