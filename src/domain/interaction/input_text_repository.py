from abc import ABC, abstractmethod


class InputTextRepository(ABC):

    @abstractmethod
    def add_context_statement(self, context_information):
        pass

    @abstractmethod
    def add_question(self, question):
        pass

    @abstractmethod
    def get_all_context_statements(self):
        pass

    @abstractmethod
    def get_all_questions(self):
        pass
