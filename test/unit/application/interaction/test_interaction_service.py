import unittest
from mock import MagicMock

from src.application.interaction.interaction_service import InteractionService
from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.interaction_state import InteractionState


class TestInteractionService(unittest.TestCase):
    _SOME_INPUT_TEXT = "input text"

    def setUp(self):
        self.interaction_state_mock = MagicMock(spec=InteractionState)
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)
        self.interaction_service = InteractionService(self.interaction_state_mock, self.input_text_processor_mock)


    def test__when__processing_input_text__then__fetch_next_interaction_state_according_to_given_input_text(
            self):
        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.interaction_state_mock.fetch_next_state.assert_called_once_with(self._SOME_INPUT_TEXT)

    def test__when__processing_input_text__then__fetched_interaction_state_is_processing_input_text_with_input_text_processor(
            self):
        next_interaction_state_mock = MagicMock(spec=InteractionState)
        self.interaction_state_mock.fetch_next_state.return_value = next_interaction_state_mock
        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        next_interaction_state_mock.process_input_text.assert_called_once_with(self._SOME_INPUT_TEXT, self.input_text_processor_mock)

