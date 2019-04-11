import abc


class Response(abc.ABC):

    def __init__(self):
        self.output = ""

    def with_output(self, output):
        self.output = output
        return self

    @abc.abstractmethod
    def print(self):
        pass

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and self.output == other.output

    def __hash__(self):
        return hash(('output', self.output))