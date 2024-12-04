import os
import sys

def check_command(message):
    print(f"SUCCESS: {message}")

def main():
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Error: Please provide both the simulation directory and the pypicongpu JSON directory name.")
        sys.exit(1)

    # Read the command-line arguments (the directory and JSON directory name)
    simulation_directory = sys.argv[1]  # First argument is the simulation directory
    pypicongpuJSON_directory_name = sys.argv[2]  # Second argument is the pypicongpu JSON directory name

    # Full path to the pypicongpu JSON directory
    pypicongpuJSON_directory_path = os.path.join(simulation_directory, pypicongpuJSON_directory_name)

    # Check if the directory exists and remove it if needed
    if os.path.exists(pypicongpuJSON_directory_path):
        print(f"Removing existing output directory: {pypicongpuJSON_directory_path}")
        try:
            os.system(f"rm -rf {pypicongpuJSON_directory_path}")
            check_command("Removing existing output directory")
        except Exception as e:
            print(f"ERROR: Failed to remove the directory. {e}")
    else:
        print(f"Directory {pypicongpuJSON_directory_name} does not exist. Proceeding...")

if __name__ == "__main__":
    main()
