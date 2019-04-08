import unittest
from mock import MagicMock

from src.application.input_text.input_text_processor_impl import InputTextProcessorImpl
from src.domain.input_text.input_text_repository import InputTextRepository
from src.domain.pipeline import Pipeline


class TestInputTextProcessorImpl(unittest.TestCase):
    _SOME_CONTEXT_STATEMENT = "context statement"
    _SOME_QUESTION = "question"
    _SOME_RESPONSE = "response"

    def setUp(self):
        self.input_text_repository_mock = MagicMock(spec=InputTextRepository)
        self.pipeline_mock = MagicMock(spec=Pipeline)
        self.input_text_processor = InputTextProcessorImpl(self.input_text_repository_mock, self.pipeline_mock)

    def test__when__processing_context_statement__then__add_given_context_statement_to_input_text_repository(self):
        self.input_text_processor.process_context_statement(self._SOME_CONTEXT_STATEMENT, self.pipeline_mock)

        self.input_text_repository_mock.add_context_statement.assert_called_once_with(self._SOME_CONTEXT_STATEMENT)

    def test__when__processing_question__then__retrieves_all_context_statements_from_input_text_repository(self):
        self.input_text_processor.process_question(self._SOME_QUESTION, self.pipeline_mock)

        self.input_text_repository_mock.get_all_context_statements.assert_called_once()

    def test__when__processing_question__then__passes_context_statements_and_given_question_to_pipeline(self):
        self.input_text_repository_mock.get_all_context_statements.return_value = [self._SOME_CONTEXT_STATEMENT]

        self.input_text_processor.process_question(self._SOME_QUESTION, self.pipeline_mock)

        self.pipeline_mock.transform.assert_called_once_with(([self._SOME_CONTEXT_STATEMENT], self._SOME_QUESTION))

    def test__when__processing_question__then__returns_appropriate_response(self):
        expected_response = self._SOME_RESPONSE
        self.input_text_repository_mock.get_all_context_statements.return_value = [self._SOME_CONTEXT_STATEMENT]
        self.pipeline_mock.transform.return_value = expected_response

        actual_response = self.input_text_processor.process_question(self._SOME_QUESTION, self.pipeline_mock)

        self.assertEqual(expected_response, actual_response)
