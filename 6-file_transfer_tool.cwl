cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/6-file_transfer.py"]

inputs:
  json_file_path:
    type: string
    inputBinding:
      prefix: "--json_file_path"
  api_key_file:
    type: File
    inputBinding:
      prefix: "--api_key_file"
  upload_type:
    type: string
    inputBinding:
      prefix: "--upload_type"
    default: "PIConGPU"
  username:
    type: string
    inputBinding:
      prefix: "--username"
    default: "afshar87"
  description:
    type: string
    inputBinding:
      prefix: "--description"
  keywords:
    type: "string[]"
    inputBinding:
      prefix: "--keywords"
      separate: true
  file_paths:
    type: "string[]" # "File[]"
    inputBinding:
      prefix: "--file_paths"
      separate: true  # Passes each file path as a separate argument

outputs:
  setup_log:
    type: stdout  # Capture the output log from stdout

stdout: output_upload_files.txt  # Redirect standard output to this file
