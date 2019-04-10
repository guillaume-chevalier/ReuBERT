import unittest

from src.api.response.response_type.question_answering_phase_response import QuestionAnsweringPhaseResponse


class TestQuestionAnsweringPhaseResponse(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.question_answering_phase_response = QuestionAnsweringPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self):
        self.question_answering_phase_response.print()
        pass