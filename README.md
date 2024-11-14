This repository provides an automated framework for managing data flow at various stages using the Common Workflow Language (CWL). It allows seamless integration of processes and tasks in scientific workflows.
To be able to use it, first one needs to install cwl on the system as well explained in [this file](https://github.com/mafshari64/common_workflow_language/blob/main/how%20to%20install%20Common%20Workflow%20Language_cwl.txt).
Afterwards, for [this file](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer_tool.cwl) define the full path for the [python code](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer.py) 
Then just need to add relevant information to [input file](https://github.com/mafshari64/common_workflow_language/blob/main/5-json_file_transfer_input.json) and on the command line run 
cwltool 5-json_file_transfer_tool.cwl 5-json_file_transfer_input.json

which send metadata to the the [website](https://fwksimulationlogger.fz-rossendorf.de/login ).
