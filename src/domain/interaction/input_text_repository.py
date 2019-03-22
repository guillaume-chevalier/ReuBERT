import abc


class InputTextRepository(abc.ABC):

    @abc.abstractmethod
    def add_context_statement(self, context_information):
        pass

    @abc.abstractmethod
    def add_question(self, question):
        pass

    @abc.abstractmethod
    def get_all_context_statements(self):
        pass

    @abc.abstractmethod
    def get_all_questions(self):
        pass
