from enum import Enum


class InteractionPhase(Enum):
    INTERACTION_INITIALIZATION_PHASE = 0
    INFORMATION_PHASE = 1
    TRANSITION_TO_QUESTION_ANSWERING_PHASE = 2
    QUESTION_ANSWERING_PHASE = 3
    EXIT_PHASE = 4

    def process_input_text(self, input_text, input_text_processor):
        if self == InteractionPhase.INTERACTION_INITIALIZATION_PHASE:
            return input_text_processor.process_initialization_statement(input_text)
        elif self == InteractionPhase.INFORMATION_PHASE:
            return input_text_processor.process_context_statement(input_text)
        elif self == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE:
            return input_text_processor.process_phase_transition_statement(input_text)
        elif self == InteractionPhase.QUESTION_ANSWERING_PHASE:
            return input_text_processor.process_question(input_text)
        elif self == InteractionPhase.EXIT_PHASE:
            return input_text_processor.process_exit_statement(input_text)
