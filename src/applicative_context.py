from src.api.cli.robot_interaction_resource_impl import CLIRobotInteractionResourceImpl
from src.application.interaction.interaction_service import InteractionService
from src.domain.pipeline import Pipeline
from src.infrastructure.persistence.interaction.in_memory_input_text_repository import InMemoryInputTextRepository
from src.infrastructure.persistence.interaction.in_memory_interaction_state import InMemoryInteractionState
from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.infrastructure.pipeline_steps.bert_natural_answer_postprocessor import BertNaturalAnswerPostprocessor


class CLIReuBERTApplicativeContext:

    def __init__(self):
        pass

    def initialize(self):
        self._initialize_domain_services()
        self._initialize_application_services()

    def _initialize_domain_services(self):
        self.pipeline = Pipeline(BertModelWrapper(), BertNaturalAnswerPostprocessor())
        self.input_text_repository = InMemoryInputTextRepository()
        self.interaction_state = InMemoryInteractionState(self.pipeline)

    def _initialize_application_services(self):
        self.interaction_service = InteractionService(self.input_text_repository, self.interaction_state)
        self.robot_interaction_resource = CLIRobotInteractionResourceImpl(self.interaction_service)

    def execute(self):
        return self.robot_interaction_resource.execute()
