from abc import ABC, abstractmethod


class InteractionState(ABC):

    @abstractmethod
    def fetch_next_state(self, input_text):
        pass

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    @abstractmethod
    def process_input_text(self, input_text_repository):
        pass
