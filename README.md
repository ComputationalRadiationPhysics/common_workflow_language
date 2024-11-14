This repository provides an automated framework for managing data flow at various stages using the Common Workflow Language (CWL). It allows seamless integration of processes and tasks in scientific workflows.
To be able to use it, first one needs to install CWL on the system as well explained in [here](https://github.com/mafshari64/common_workflow_language/blob/main/how%20to%20install%20Common%20Workflow%20Language_cwl.txt).
Afterward, define the full path for the [python code](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer.py) for [this file](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer_tool.cwl).
Then one just needs to add relevant information to [input file](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer_input.json) and on the command line run 
cwltool 5-json_file_transfer_tool.cwl 5-json_file_transfer_input.json

which send metadata to the the [website](https://fwksimulationlogger.fz-rossendorf.de/login ).
