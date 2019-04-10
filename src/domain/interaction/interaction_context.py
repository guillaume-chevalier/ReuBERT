from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionContext:
    _INITIAL_INTERACTION_PHASE = InteractionPhase.INFORMATION_PHASE

    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions."
    SWITCHING_TO_EXIT_PHASE_MESSAGE = "I have no more questions to ask."

    def __init__(self):
        self.current_interaction_phase = self._INITIAL_INTERACTION_PHASE

    def fetch_next_interaction_phase(self, input_text):
        next_interaction_phase = self.current_interaction_phase
        if self.current_interaction_phase == InteractionPhase.INFORMATION_PHASE:
            next_interaction_phase = self._fetch_next_phase_from_information_phase(input_text)
        elif self.current_interaction_phase == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE or \
                self.current_interaction_phase == InteractionPhase.QUESTION_ANSWERING_PHASE:
            next_interaction_phase = self._fetch_next_phase_from_question_answering_phase(input_text)
        self.current_interaction_phase = next_interaction_phase
        return next_interaction_phase

    def _fetch_next_phase_from_information_phase(self, input_text):
        if input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            return InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE
        return InteractionPhase.INFORMATION_PHASE

    def _fetch_next_phase_from_question_answering_phase(self, input_text):
        if input_text == self.SWITCHING_TO_EXIT_PHASE_MESSAGE:
            return InteractionPhase.EXIT_PHASE
        return InteractionPhase.QUESTION_ANSWERING_PHASE
