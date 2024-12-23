cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/2-git_clone_picmi.py"]

inputs:
  picmi_git_path:
    type: string
    inputBinding:
      position: 1  # Pass the git URL as the first argument
  picmi_local_dir:
    type: string
    inputBinding:
      position: 2  # Pass the repo directory as the second argument

outputs:
  setup_log:
    type: stdout  # Capture the output log from stdout

stdout: output_clone_picmi.txt  # Redirect standard output to this file
