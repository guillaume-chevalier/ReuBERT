from src.api.response.response import Response
from src.api.response.response_type.response_tag import ResponseTag


class SwitchingToQuestionAnsweringPhaseResponse(Response):

    def print(self):
        print("\n" + ResponseTag.GATHER_INFORMATION_TAG.__str__().format(self.output), end="\n")
        print(ResponseTag.ENTER_QUESTION_TAG.__str__(), end="\n")