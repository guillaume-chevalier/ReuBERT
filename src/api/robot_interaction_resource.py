import abc

from src.application.interaction.interaction_service import InteractionService


class RobotInteractionResource(abc.ABC):

    def __init__(self, interaction_service: InteractionService):
        self.interaction_service: InteractionService = interaction_service

    @abc.abstractmethod
    def execute(self):
        pass
