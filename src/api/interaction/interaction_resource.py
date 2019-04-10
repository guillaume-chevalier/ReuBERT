import abc


class InteractionResource(abc.ABC):

    def __init__(self, interaction_service, response_factory):
        self.interaction_service = interaction_service
        self.response_factory = response_factory

    @abc.abstractmethod
    def execute(self):
        pass
