import unittest

from src.api.response.response_type.ending_interaction_response import EndingInteractionResponse


class TestEndingInteractionResponse(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.ending_interaction_response = EndingInteractionResponse().with_output(self._SOME_REUBERT_OUTPUT)

    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self):
        self.ending_interaction_response.print()
        pass
