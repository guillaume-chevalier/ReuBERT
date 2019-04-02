from src.api.cli.robot_interaction_resource_impl import CLIRobotInteractionResourceImpl
from src.application.interaction.interaction_service import InteractionService
from src.domain.pipeline import Pipeline
from src.domain.pipeline_steps.natural_answer_postprocessor_interface import NaturalAnswerPostprocessorInterface
from src.infrastructure.bert_model_wrapper import BertModelWrapper
from src.infrastructure.persistence.interaction.in_memory_input_text_repository import InMemoryInputTextRepository
from src.infrastructure.persistence.interaction.in_memory_interaction_state import InMemoryInteractionState

if __name__ == "__main__":
    # 1. Initialize Domain Service(s).
    pipeline = Pipeline(BertModelWrapper(), NaturalAnswerPostprocessorInterface())
    input_text_repository = InMemoryInputTextRepository()
    interaction_state = InMemoryInteractionState(pipeline)

    # 2. Initialize Application Service(s).
    interaction_service = InteractionService(input_text_repository, interaction_state)

    # 3. Execute CLI main applicative loop.
    CLIRobotInteractionResourceImpl(interaction_service).execute()
