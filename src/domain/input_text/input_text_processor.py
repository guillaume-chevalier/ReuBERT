from abc import ABC, abstractmethod


class InputTextProcessor(ABC):

    @abstractmethod
    def process_context_statement(self, context_statement):
        pass

    @abstractmethod
    def process_phase_transition_statement(self, phase_transition_statement):
        pass

    @abstractmethod
    def process_question(self, question):
        pass

    @abstractmethod
    def process_exit_statement(self, exit_statement):
        pass
