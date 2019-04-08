import pytest
import unittest

from src.infrastructure.persistence.interaction.in_memory_input_text_repository import InMemoryInputTextRepository


class TestInMemoryInputTextRepository(unittest.TestCase):

    def setUp(self):
        self.input_text_repository = InMemoryInputTextRepository()

    def test__repository_containing_context_statements__when__get_all_context_statements__then__returns_all_context_statements(
        self
    ):
        some_context_statement = "some context statement"
        self.input_text_repository.add_context_statement(some_context_statement)

        actual_context_statements = self.input_text_repository.get_all_context_statements()

        expected_context_statements = [some_context_statement]
        self.assertEqual(expected_context_statements, actual_context_statements)

    def test__repository_containing_questions__when__get_all_questions__then__returns_all_questions(self):
        some_question = "some context statement"
        self.input_text_repository.add_question(some_question)

        actual_questions = self.input_text_repository.get_all_questions()

        expected_questions = [some_question]
        self.assertEqual(expected_questions, actual_questions)


if __name__ == "__main__":
    pytest.main(__file__)
