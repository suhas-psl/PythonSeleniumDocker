import json
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
resources_dir = os.path.join(proj_dir, "resources")
test_data_path = os.path.join(resources_dir, "test_data.json")


def get_registration_data(attri):
    with open(test_data_path, "r") as fh:
        data_dict= json.load(fh)
    return data_dict[attri]