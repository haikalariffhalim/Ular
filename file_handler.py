import json


def read_json(file_path):

    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        print(f"Loaded data from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
