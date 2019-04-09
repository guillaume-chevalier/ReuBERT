import abc


class InteractionResource(abc.ABC):

    def __init__(self, interaction_service):
        self.interaction_service = interaction_service

    @abc.abstractmethod
    def execute(self):
        pass
