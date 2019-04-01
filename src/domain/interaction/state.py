from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def on_input_text_reception(self, input_text):
        pass
