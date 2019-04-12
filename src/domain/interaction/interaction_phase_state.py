from abc import ABC, abstractmethod


class InteractionPhaseState(ABC):

    @abstractmethod
    def fetch_next_interaction_phase(self, input_text):
        pass

    @abstractmethod
    def process_input_text(self, input_text, input_text_processor):
        pass

    def __eq__(self, other):
        return isinstance(other, self.__class__)
