import unittest
from unittest.mock import patch, call

from src.api.response.response_tag import ResponseTag
from src.api.response.response_type.initiating_interaction_response import InitiatingInteractionResponse


class TestInitiatingInteractionResponse(unittest.TestCase):

    def setUp(self):
        self.initiating_interaction_response = InitiatingInteractionResponse()

    @patch('builtins.print')
    def test__when__printing__then__prints_reuBERT_output_in_appropriate_response_format(self, print_mock):
        expected_response_format = ResponseTag.GREETING_TAG.__str__() + "\n" \
                                   + ResponseTag.ENTER_INFORMATION_TAG.__str__() + "\n"

        self.initiating_interaction_response.print()

        print_mock.assert_has_calls([call(expected_response_format)], any_order=False)
