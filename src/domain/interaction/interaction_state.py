from abc import ABC, abstractmethod


class InteractionState(ABC):

    @abstractmethod
    def fetch_next_state(self, input_text):
        pass

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    # TODO: the InputTextProcessor will contain the bert_model_wrapper
    @abstractmethod
    def process_input_text(self, input_text, input_text_repository, bert_model_wrapper):
        pass
