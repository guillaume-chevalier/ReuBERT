import abc


class RobotInteractionResourceInterface(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass
