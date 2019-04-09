import os
import json

def extract_question_from_coqa():
    with open(os.path.join(__file__, '../coqa-dev-v1.0.json'), encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data



extract_question_from_coqa()
