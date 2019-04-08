from src.domain.interaction.ending_dialogue_interaction_state import EndingDialogueInteractionState
from src.domain.interaction.receiving_context_statement_interaction_state import \
    ReceivingContextStatementInteractionState
from src.domain.interaction.receiving_question_interaction_state import ReceivingQuestionInteractionState


class InteractionContext:
    _INITIAL_INTERACTION_STATE = ReceivingContextStatementInteractionState()

    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions."
    SWITCHING_TO_INTERACTION_ENDING_PHASE_MESSAGE = "I have no more questions to ask."

    def __init__(self):
        self.interaction_state = self._INITIAL_INTERACTION_STATE

    def fetch_next_interaction_state(self, input_text):
        next_interaction_state = self.interaction_state
        if input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            next_interaction_state = ReceivingQuestionInteractionState()
        elif input_text == self.SWITCHING_TO_INTERACTION_ENDING_PHASE_MESSAGE:
            next_interaction_state = EndingDialogueInteractionState()
        return next_interaction_state
