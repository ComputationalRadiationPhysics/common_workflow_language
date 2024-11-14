This repository provides an automated framework for managing data flow at various stages using the [Common Workflow Language (CWL)](https://www.commonwl.org/). It allows seamless integration of processes and tasks in scientific workflows.
To be able to use it, first one needs to install CWL on the system as well explained [here](https://github.com/mafshari64/common_workflow_language/blob/main/how%20to%20install%20Common%20Workflow%20Language_cwl.txt).
Each step contains:
- an input.json file containing required input information, e.g. [input.json file](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json) determines the path of cloning the PIConGPU [(picongpu_git_path)](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json#L2), and where to save it in your local directory [(picongpu_local_dir)](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_input.json#L3).
- a Python code doing the tasks.
- a tool.cwl file written in the CWL language that reads inputs from the .json file, runs the Python code and processes all steps defined there. Importantly, one should define the **FULL** path of the Python code used in each .cwl file, e.g.
[`baseCommand` in 1-git_clone_picongpu_tool.cwl](https://github.com/mafshari64/common_workflow_language/blob/main/1-git_clone_picongpu_tool.cwl#L4).  
To run a step, one just needs to open a terminal where these files are present and type in the command line cwltool, relevant .cwl and .json files, e.g.:

`cwltool 5-json_file_transfer_tool.cwl 5-json_file_transfer_input.json`

which sends **metadata** to [this website](https://fwksimulationlogger.fz-rossendorf.de/login).