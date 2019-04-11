import unittest
from mock import MagicMock

from src.application.interaction.interaction_service import InteractionService
from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.interaction_initialization_phase import InteractionInitializationPhase


class TestInteractionService(unittest.TestCase):

    _SOME_INPUT_TEXT = "input text"
    _SOME_OUTPUT_TEXT = "output text"

    def setUp(self):
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)
        self.interaction_service = InteractionService(self.input_text_processor_mock)

    def test__when__initializing__then__has_interaction_initialization_phase_as_initial_interaction_phase(self):
        expected_initial_interaction_phase = InteractionInitializationPhase()

        actual_initial_interaction_phase = self.interaction_service.interaction_phase

        self.assertEqual(expected_initial_interaction_phase, actual_initial_interaction_phase)

    def test__when__initiating_interaction__then__interaction_phase_processes_empty_input_text_with_input_text_processor(
        self
    ):
        interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock

        self.interaction_service.initiate_interaction()

        interaction_phase_mock.process_input_text.assert_called_once_with("", self.input_text_processor_mock)

    def test__when__initiating_interaction__then__returns_output_from_processing_in_tuple_with_interaction_phase(self):
        interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock
        interaction_phase_mock.process_input_text.return_value = self._SOME_OUTPUT_TEXT
        expected_response = self._SOME_OUTPUT_TEXT, interaction_phase_mock

        actual_response = self.interaction_service.initiate_interaction()

        self.assertEqual(expected_response, actual_response)

    def test__when__processing_input_text__then__interaction_phase_fetches_next_interaction_phase_according_to_given_input_text(
        self
    ):
        interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock

        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        interaction_phase_mock.fetch_next_interaction_phase.assert_called_once_with(self._SOME_INPUT_TEXT)

    def test__when__processing_input_text__then__fetched_interaction_phase_is_processing_input_text_with_input_text_processor(
        self
    ):
        interaction_phase_mock = MagicMock()
        next_interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock
        interaction_phase_mock.fetch_next_interaction_phase.return_value = next_interaction_phase_mock

        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        next_interaction_phase_mock.process_input_text.assert_called_once_with(
            self._SOME_INPUT_TEXT, self.input_text_processor_mock
        )

    def test__when__processing_input_text__then__current_interaction_phase_is_set_to_fetched_interaction_state(self):
        interaction_phase_mock = MagicMock()
        next_interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock
        interaction_phase_mock.fetch_next_interaction_phase.return_value = next_interaction_phase_mock

        self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.assertEqual(self.interaction_service.interaction_phase, next_interaction_phase_mock)

    def test__when__processing_input_text__then__returns_output_from_processing_in_tuple_with_next_interaction_phase(
        self
    ):
        interaction_phase_mock = MagicMock()
        next_interaction_phase_mock = MagicMock()
        self.interaction_service.interaction_phase = interaction_phase_mock
        interaction_phase_mock.fetch_next_interaction_phase.return_value = next_interaction_phase_mock
        next_interaction_phase_mock.process_input_text.return_value = self._SOME_OUTPUT_TEXT
        expected_response = self._SOME_OUTPUT_TEXT, next_interaction_phase_mock

        actual_response = self.interaction_service.process_input_text(self._SOME_INPUT_TEXT)

        self.assertEqual(expected_response, actual_response)
