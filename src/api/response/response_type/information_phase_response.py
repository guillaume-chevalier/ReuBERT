from src.api.response.response_type.response_tag import ResponseTag


class InformationPhaseResponse:

    def __init__(self):
        self.output = ""

    def with_output(self, output):
        self.output = output

    def print(self):
        print("\n" + ResponseTag.GATHER_INFORMATION_TAG.__str__().format(self.output), end="\n")
        print(ResponseTag.ENTER_INFORMATION_TAG.__str__(), end="\n")

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
               and self.output == other.output

    def __hash__(self):
        return hash(('output', self.output))
