cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python3", "/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/3-1-update_profile.py"]

inputs:
  profile_name:
    type: string
    inputBinding:
      position: 1  # Pass the profile name as the first argument

  new_my_mail:
    type: string
    inputBinding:
      position: 2  # Pass the new mail as the second argument

  new_my_mailnotify:
    type: string
    inputBinding:
      position: 3  # Pass the new mailnotify as the third argument

  picsrc:
    type: string
    inputBinding:
      position: 4  # Pass the picsrc path as the fourth argument

  tbg_partition:
    type: string
    inputBinding:
      position: 5  # Pass the tbg_partition as the fifth argument

  simulation_output_path:
    type: string
    inputBinding:
      position: 6  # Pass the simulation_output_path as the sixth argument

outputs:
  profile_file:
    type: File
    outputBinding:
      glob: "profile/fwkt_v100_picongpu.profile"  # This will capture the output profile file and save it in the current working directory under "profile"

# outputs:
  log_file:
    type: stdout
stdout: output_update_profile.txt  # Redirect standard output to this file
