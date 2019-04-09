from enum import Enum


class InteractionPhase(Enum):
    INFORMATION_PHASE = 0
    TRANSITION_TO_QUESTION_ANSWERING_PHASE = 1
    QUESTION_ANSWERING_PHASE = 2
    EXIT_PHASE = 3

    def process_input_text(self, input_text, input_text_processor):
        if self == InteractionPhase.INFORMATION_PHASE:
            return input_text_processor.process_context_statement(input_text)
        elif self == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE:
            return "Ok. Ask me your questions."
        elif self == InteractionPhase.QUESTION_ANSWERING_PHASE:
            return input_text_processor.process_question(input_text)
        elif self == InteractionPhase.EXIT_PHASE:
            return input_text_processor.process_exit_statement(input_text)
