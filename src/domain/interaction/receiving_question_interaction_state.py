from src.domain.interaction.receiving_statement_context_interaction_state import ReceivingStatementContextInteractionState
from src.domain.interaction.interaction_state import InteractionState
from src.infrastructure.user_input_question_pair import UserInputQuestionPair


class ReceivingQuestionInteractionState(InteractionState):
    SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE = "I have no more questions to ask"

    def fetch_next_state(self, input_text):
        if input_text == self.SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE:
            return ReceivingStatementContextInteractionState()
        return self

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    # TODO: change the message to the actual response
    def process_input_text(self, input_text, input_text_repository, bert_model_wrapper):
        context_statements = input_text_repository.get_all_context_statements()
        response = bert_model_wrapper.transform(UserInputQuestionPair(context_statements, input_text))
        return response