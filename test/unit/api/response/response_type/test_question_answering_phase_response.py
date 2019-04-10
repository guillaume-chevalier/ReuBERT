import unittest
from unittest.mock import patch, call

from src.api.response.response_tag import ResponseTag
from src.api.response.response_type.question_answering_phase_response import QuestionAnsweringPhaseResponse


class TestQuestionAnsweringPhaseResponse(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.question_answering_phase_response = QuestionAnsweringPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

    @patch('builtins.print')
    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self, print_mock):
        expected_response_format = "\n" + ResponseTag.ANSWER_QUESTION_TAG.__str__().format(self._SOME_REUBERT_OUTPUT) + "\n" \
                                   + ResponseTag.ENTER_QUESTION_TAG.__str__() + "\n"

        self.question_answering_phase_response.print()

        print_mock.assert_has_calls([call(expected_response_format)], any_order=False)