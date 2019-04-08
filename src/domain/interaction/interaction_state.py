from abc import ABC, abstractmethod


class InteractionState(ABC):

    @abstractmethod
    def process_input_text(self, input_text, input_text_processor):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass
