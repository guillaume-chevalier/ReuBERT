import unittest
import pytest
import os

from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper

INPUT = (
    "The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th "
    "centuries gave their name to Normandy, a region in France. They were descended from Norse (\"Norman\" comes from "
    "\"Norseman\") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, "
    "agreed to swear fealty to King Charles III of West Francia. Through generations of assimilation and mixing with "
    "the native Frankish and Roman-Gaulish populations, their descendants would gradually merge with the "
    "Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged "
    "initially in the first half of the 10th century, and it continued to evolve over the succeeding centuries.",
    "In what country is Normandy located?"
)

EXPECTED_OUTPUT = [
    (0.9996078645059949, 'France'), (0.0002669493485279948, 'France.'),
    (
        4.7795265362342654e-05,
        'France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'
    ),
    (
        3.0785827498947834e-05,
        'France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland and Norway'
    ), (1.4057721531176204e-05, 'in France'), (1.3250716703090425e-05, 'Normandy, a region in France'),
    (
        8.06727339463416e-06,
        'French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France'
    ), (8.060427117150136e-06, 'a region in France'), (1.7120437138804593e-06, 'region in France'),
    (
        1.4416956618215133e-06,
        'France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland'
    ), (3.754171748528642e-09, 'in France.'), (3.5386578247532317e-09, 'Normandy, a region in France.'),
    (2.152569866828721e-09, 'a region in France.'), (1.507324631299853e-09, 'Denmark'),
    (9.708960863030124e-10, 'Denmark, Iceland and Norway'),
    (
        6.993905850866089e-10,
        'Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia.'
    ),
    (
        6.721561072396455e-10,
        'in France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'
    ), (6.657576659787132e-10, '.'),
    (
        6.335699663371694e-10,
        'Normandy, a region in France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'
    ), (5.799991157924552e-10, '')
]


class TestModelWrapper(unittest.TestCase):

    def setUp(self):
        self.bert_wrapper = BertModelWrapper()

    def test__given__some_test_data__when__bert_model_wrapper__then__get_good_results(self):
        if os.environ.get("CI") is not None:
            return
        result_output = self.bert_wrapper.transform(INPUT)

        assert result_output == EXPECTED_OUTPUT


if __name__ == "__main__":
    pytest.main(__file__)
