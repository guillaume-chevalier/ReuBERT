from src.domain.interaction.interaction_phase_state import InteractionPhaseState


class ExitPhase(InteractionPhaseState):

    def fetch_next_interaction_phase(self, input_text):
        return self

    def process_input_text(self, input_text, input_text_processor):
        return input_text_processor.process_exit_statement(input_text)