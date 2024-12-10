cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/5-json_metadata_transfer.py"]

inputs:
  json_file_path:
    type: string
    inputBinding:
      prefix: "--json_file_path"  # Pass the directory as a command-line argument
      # loadContents: true  # pass the contents of the file or directory as input, not just their paths.

  api_key_file:
    type: File
    inputBinding:
      prefix: "--api_key_file"  # Pass the file as a command-line argument
      # loadContents: true  # pass the contents of the file or directory as input, not just their paths.

  upload_type:
    type: string
    inputBinding:
      prefix: "--upload_type"
    default: "PIConGPU"  # Default value if not specified

  username:
    type: string
    inputBinding:
      prefix: "--username"
    default: "afshar87"  # Default value if not specified

  description:
    type: string
    inputBinding:
      prefix: "--description"  # Passes the description as a command-line argument

  keywords:
    type: "string[]"
    inputBinding:
      prefix: "--keywords"  # Prefix used to handle the list as separate arguments
      separate: true  # Correctly specify 'true' to separate the list items into individual arguments

outputs:
  setup_log:
    type: stdout  # Capture the output log from stdout

stdout: output_upload_metadata.txt  # Redirect standard output to this file
