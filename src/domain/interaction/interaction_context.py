from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionContext:
    _INITIAL_INTERACTION_PHASE = InteractionPhase.INFORMATION_PHASE

    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions."
    SWITCHING_TO_EXIT_PHASE_MESSAGE = "I have no more questions to ask."

    def __init__(self):
        self.interaction_phase = self._INITIAL_INTERACTION_PHASE

    def fetch_next_interaction_phase(self, input_text):
        next_interaction_phase = self.interaction_phase
        if input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            next_interaction_phase = InteractionPhase.QUESTION_ANSWERING_PHASE
        elif input_text == self.SWITCHING_TO_EXIT_PHASE_MESSAGE:
            next_interaction_phase = InteractionPhase.EXIT_PHASE
        return next_interaction_phase
