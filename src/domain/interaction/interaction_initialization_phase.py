from src.domain.interaction.information_phase import InformationPhase
from src.domain.interaction.interaction_phase_state import InteractionPhaseState


class InteractionInitializationPhase(InteractionPhaseState):

    def fetch_next_interaction_phase(self, input_text):
        return InformationPhase()

    def process_input_text(self, input_text, input_text_processor):
        return input_text_processor.process_initialization_statement(input_text)