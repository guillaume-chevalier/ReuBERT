import json
import os

import pytest
import stringdist

# Todo : put different levels of questions : easy , medium, hard, impossible
def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


class TestSquad():
    pass