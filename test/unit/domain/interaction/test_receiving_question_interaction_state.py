import unittest
from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.receiving_question_interaction_state import ReceivingQuestionInteractionState


class TestReceivingQuestionInteractionState(unittest.TestCase):

    _SOME_INPUT_TEXT = "some question"

    def setUp(self):
        self.receivingQuestionInteractionState = ReceivingQuestionInteractionState()
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__when__processing_input_text__then__input_text_processor_processes_given_question(self):
        self.receivingQuestionInteractionState.process_input_text(self._SOME_INPUT_TEXT,  self.input_text_processor_mock)

        self.input_text_processor_mock.process_question.assert_called_once_with(self._SOME_INPUT_TEXT)
