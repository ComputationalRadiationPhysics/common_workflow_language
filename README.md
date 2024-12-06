This repository provides an automated framework for managing data flow at various stages using the Common Workflow Language (CWL). It allows seamless integration of processes and tasks in scientific workflows.
To be able to use it, first one needs to install CWL on the system as well explained [here](https://github.com/mafshari64/common_workflow_language/blob/main/how%20to%20install%20Common%20Workflow%20Language_cwl.txt).
Each step contains:

- a Python code doing the tasks.
- a tool.cwl file written in the CWL language that reads inputs from the .json file, runs the Python code and processes all steps defined there. Importantly, one should define the **FULL** path for the Python code used in each .cwl file, e.g.
[`baseCommand` in 1-git_clone_picongpu_tool.cwl](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_tool.cwl#L4). View the 
- an input.json file containing required input information, e.g. [input.json file](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json) determines the path for cloning the PIConGPU [picongpu_git_path](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json#L2C6-L2C23), where to save in your local director [picongpu_local_dir](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json#L3C6-L3C24) and where the output file of tool.cwl file [picongpu_input_json]()

- 
Afterward, to use one of them, o [python code](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer.py) for [this .cwl file](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer_tool.cwl).
Then one just needs to add relevant information to  and on the command line run 


`cwltool 5-json_file_transfer_tool.cwl 5-json_file_transfer_input.json`

which sends **metadata** to [this website](https://fwksimulationlogger.fz-rossendorf.de/login).
