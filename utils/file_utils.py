import json


def write_dict(input_dict, file_name):
    with open(file_name, 'w') as f:
        json.dump(input_dict, f, indent=2)
        f.close()


def read_json(file_name):
    with open(file_name, 'r') as f:
        input_dict = json.load(f)
        f.close()
    return input_dict
