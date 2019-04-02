from src.domain.interaction.receiving_question_interaction_state import ReceivingQuestionInteractionState
from src.domain.interaction.interaction_state import InteractionState


class ReceivingStatementContextInteractionState(InteractionState):
    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions"
    ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE = "Can you give me more information please?"

    def fetch_next_state(self, input_text):
        if input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            return ReceivingQuestionInteractionState()
        return self

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    def process_input_text(self, input_text, input_text_repository, bert_model_wrapper):
        input_text_repository.add_context_statement(input_text)
        return self.ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE
