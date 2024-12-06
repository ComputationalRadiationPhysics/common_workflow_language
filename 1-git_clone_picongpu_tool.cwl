cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/1-git_clone_picongpu.py"]  # Replace with the name of your shell script

inputs:
  picongpu_git_path:
    type: string
    inputBinding:
      position: 1  # Pass the JSON file path as the first argument
  picongpu_local_dir:
    type: string
    inputBinding:
      position: 2  # Pass the repo directory as the second argument
  picongpu_input_json:
    type: string
    inputBinding:
      position: 3  # Pass the log file path as the third argument

outputs:
  setup_log:
    type: stdout  # Capture the output log from stdout

stdout: output_clone_picongpu.txt  # Redirect standard output to this file
