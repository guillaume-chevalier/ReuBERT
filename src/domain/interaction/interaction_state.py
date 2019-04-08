from abc import ABC, abstractmethod


class InteractionState(ABC):

    @abstractmethod
    def fetch_next_state(self, input_text):
        pass

    @abstractmethod
    def process_input_text(self, input_text, input_text_processor):
        pass
