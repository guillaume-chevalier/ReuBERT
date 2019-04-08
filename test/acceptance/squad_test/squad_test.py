import json
import os

import pytest
import stringdist

def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


SQUAD_DATA_SET = load_json_file_test('squad_questions_beautified.json')

class TestSquad():
    @classmethod
    def setup_class(cls):
        pass