cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/3-check_pypicongpuJSON_directory_name.py"]

inputs:
  simulation_directory:
    type: string
    inputBinding:
      position: 1  # Pass the repo directory as the second argument    type: string
  pypicongpuJSON_directory_name:
    type: string
    inputBinding:
      position: 2  # Pass the repo directory as the second argument

outputs:
  log_file:
    type: stdout

stdout: output-check_pypicongpuJSON_directory_name.txt
