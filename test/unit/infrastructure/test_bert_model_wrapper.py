import unittest
from typing import List, Any, Union, Tuple, Dict

import pytest
import os

from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.domain.pipeline_steps.question_answering_model import TextQuestionAnswerTriplet, UserInputAndQuestionTuple

INPUT: UserInputAndQuestionTuple = (
    [
        "The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France.",
        "They were descended from Norse (\"Norman\" comes from \"Norseman\") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear ",
        "fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would ",
        "gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th",
        " century, and it continued to evolve over the succeeding centuries."],
    "In what country is Normandy located?"
)

EXPECTED_OUTPUT: TextQuestionAnswerTriplet = \
    [([
          'The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France.',
          'They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear ',
          'fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would ',
          'gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th',
          ' century, and it continued to evolve over the succeeding centuries.'],
      'In what country is Normandy located?',
      [(0.9996078633149131, 'France'), (0.0002669500164904331, 'France.'), (
          4.7795487513854006e-05,
          'France.They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'),
       (3.078599995070936e-05,
        'France.They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland and Norway'),
       (1.4057741624172056e-05, 'in France'),
       (1.3250779871793082e-05, 'Normandy, a region in France'), (
           8.067325316660916e-06,
           'French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France'),
       (8.060411733515779e-06, 'a region in France'),
       (1.7120461609404018e-06, 'region in France'), (1.4417018472034922e-06,
                                                      'France.They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland'),
       (3.754186512645245e-09, 'in France.'),
       (3.5386835529242774e-09, 'Normandy, a region in France.'),
       (2.1525711472958317e-09, 'a region in France.'),
       (1.507338106096412e-09, 'Denmark'),
       (9.709056915997677e-10, 'Denmark, Iceland and Norway'), (
           6.99394252712477e-10,
           'Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia.'),
       (6.721601929410085e-10,
        'in France.They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'),
       (6.657609191378117e-10, '.'), (6.335759322769482e-10,
                                      'Normandy, a region in France.They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark'),
       (5.800012584850742e-10, '')])]


class TestModelWrapper(unittest.TestCase):

    def setUp(self):
        self.bert_wrapper = BertModelWrapper()

    @pytest.mark.skipif(os.environ.get("CI") is not None,
                        reason="Disable test if in CI, because it needs a downloaded model")
    def test__given__some_test_data__when__bert_model_wrapper__then__get_good_results(self):
        result_output = self.bert_wrapper.transform([INPUT])

        assert result_output == EXPECTED_OUTPUT


if __name__ == "__main__":
    pytest.main(__file__)
