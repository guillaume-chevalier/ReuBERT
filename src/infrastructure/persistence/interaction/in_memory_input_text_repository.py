from src.domain.input_text.input_text_repository import InputTextRepository


class InMemoryInputTextRepository(InputTextRepository):

    def __init__(self):
        self.context_statements = []
        self.questions = []

    def add_context_statement(self, context_statement):
        self.context_statements.append(context_statement)

    def add_question(self, question):
        self.questions.append(question)

    def get_all_context_statements(self):
        return [context_statement for context_statement in self.context_statements]

    def get_all_questions(self):
        return [question for question in self.questions]
