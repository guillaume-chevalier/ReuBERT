import unittest
from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.ending_dialogue_interaction_state import EndingDialogueInteractionState


class TestEndingDialogueInteractionState(unittest.TestCase):

    _SOME_INPUT_TEXT = "ending dialogue"

    def setUp(self):
        self.endingDialogueInteractionState = EndingDialogueInteractionState()
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__when__processing_input_text__then__returns_appropriate_response(self):
        expected_response = EndingDialogueInteractionState.EXIT_CODE

        actual_response = self.endingDialogueInteractionState.process_input_text(
            self._SOME_INPUT_TEXT, self.input_text_processor_mock
        )

        self.assertEqual(expected_response, actual_response)