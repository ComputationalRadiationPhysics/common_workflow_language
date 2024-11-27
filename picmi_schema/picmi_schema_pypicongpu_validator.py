# python picmi_schema_pypicongpu_validator.py


import json
import os

schema_path = "picmi_schema.json"
pypicongpu_json_path = "/home/afshar87/afshari/simulation/simulation_auto/testPICMI-v2/picmi_inputfile_ionization-v2.py"
# pypicongpu_json_path = "./testPICMI-v2/lwfa_ionization_v2/pypicongpu.json"
 
# print("File exists:", os.path.exists(schema_path))
# print("File exists:", os.path.exists(pypicongpu_json_path))





# Define the color codes for terminal output
RED = '\033[91m'
ORANGE = '\033[38;5;214m'
BLUE = '\033[94m'
RESET = '\033[0m'


def validate_json_against_schema(schema_path, pypicongpu_json_path):
    # Load the schema and pypicongpu JSON files
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    with open(pypicongpu_json_path) as pypicongpu_file:
        pypicongpu_json = json.load(pypicongpu_file)

    # Flatten the schema to easily access properties (recursive)
    def flatten_schema(schema, parent_key=''):
        items = {}
        if isinstance(schema, dict):
            for key, value in schema.items():
                new_key = parent_key + '.' + key if parent_key else key
                if isinstance(value, dict):
                    items.update(flatten_schema(value, new_key))
                else:
                    items[new_key] = value
        return items

    # Flatten the JSON file similarly
    def flatten_json(json_data, parent_key=''):
        items = {}
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                new_key = parent_key + '.' + key if parent_key else key
                if isinstance(value, dict):
                    items.update(flatten_json(value, new_key))
                else:
                    items[new_key] = value
        return items

    # Flatten both schema and pypicongpu JSON for easier comparison
    schema_properties = flatten_schema(schema)
    pypicongpu_properties = flatten_json(pypicongpu_json)

    # Check for missing parameters and type mismatches
    missing_params = []
    type_mismatches = []
    extra_params = []

    # Check for missing parameters in the schema
    for key in pypicongpu_properties:
        if key not in schema_properties:
            extra_params.append(key)
        elif type(pypicongpu_properties[key]) != type(schema_properties[key]):
            type_mismatches.append(key)
    
    # Print the warnings
    for key in extra_params:
        print(BLUE + "Extra parameter in JSON file: " + key + RESET)

    for key in type_mismatches:
        print(ORANGE + "Type mismatch for parameter '" + key + "': " + str(type(pypicongpu_properties[key])) + " (in JSON) vs " + str(type(schema_properties[key])) + " (in schema)" + RESET)
    
    # Check if there are missing parameters (in the schema but not in the JSON)
    for key in schema_properties:
        if key not in pypicongpu_properties:
            print(RED + "Missing parameter in JSON file: " + key + RESET)



validate_json_against_schema(schema_path, pypicongpu_json_path)
