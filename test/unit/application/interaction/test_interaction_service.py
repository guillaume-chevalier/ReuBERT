import unittest
from mock import MagicMock

from src.application.interaction.interaction_service import InteractionService
from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.interaction_context import InteractionContext
from src.domain.interaction.interaction_phase import InteractionPhase


class TestInteractionService(unittest.TestCase):

    _SOME_INPUT_TEXT = "some input text"
    _SOME_RESPONSE_TO_INPUT_TEXT = "some response to input text"
    _SOME_INTERACTION_PHASE = InteractionPhase.EXIT_PHASE

    def setUp(self):
        self.interaction_context_mock = MagicMock(spec=InteractionContext)
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)
        self.interaction_service = InteractionService(self.interaction_context_mock, self.input_text_processor_mock)

    def test__when__processing_input_text__then__interaction_context_processes_input_text_with_input_text_processor(self):
        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.interaction_context_mock.process_input_text.assert_called_once_with(self._SOME_INPUT_TEXT,
                                                                                 self.input_text_processor_mock)

    def test__when__processing_input_text__then__interaction_context_fetches_next_interaction_phase_according_to_given_input_text(self):
        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.interaction_context_mock.fetch_next_interaction_phase.assert_called_once_with(self._SOME_INPUT_TEXT)

    def test__when__processing_input_text__then__returns_appropriate_response_concatenated_with_next_interaction_phase(
            self):
        expected_response = self._SOME_RESPONSE_TO_INPUT_TEXT, self._SOME_INTERACTION_PHASE
        self.interaction_context_mock.process_input_text.return_value = self._SOME_RESPONSE_TO_INPUT_TEXT
        self.interaction_context_mock.get_interaction_phase.return_value = self._SOME_INTERACTION_PHASE

        actual_response = self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.interaction_context_mock.process_input_text.assert_called_once_with(self._SOME_INPUT_TEXT,
                                                                                 self.input_text_processor_mock)
        self.assertEqual(expected_response, actual_response)




