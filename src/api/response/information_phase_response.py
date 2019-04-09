from src.api.response.response_tag import ResponseTag


class InformationPhaseResponse:

    def __init__(self):
        self.output = ""

    def with_output(self, output):
        self.output = output
        return self

    def print(self):
        print("\n" + ResponseTag.GATHER_INFORMATION_TAG.__str__().format(self.output), end="\n")
        print(ResponseTag.ENTER_INFORMATION_TAG.__str__(), end="\n")
