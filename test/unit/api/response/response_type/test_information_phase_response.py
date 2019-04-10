import unittest

from src.api.response.response_type.information_phase_response import InformationPhaseResponse


class TestInformationPhaseResponse(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.information_phase_response = InformationPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self):
        self.information_phase_response.print()
        pass