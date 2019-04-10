from src.api.response.response import Response
from src.api.response.response_tag import ResponseTag


class SwitchingToQuestionAnsweringPhaseResponse(Response):

    def print(self):
        print(
            "\n" + ResponseTag.GATHER_INFORMATION_TAG.__str__().format(self.output) + "\n" +
            ResponseTag.ENTER_QUESTION_TAG.__str__() + "\n"
        )
