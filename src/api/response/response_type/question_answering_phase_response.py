from src.api.response.response import Response
from src.api.response.response_tag import ResponseTag


class QuestionAnsweringPhaseResponse(Response):

    def print(self):
        print(
            "\n" + ResponseTag.ANSWER_QUESTION_TAG.__str__().format(self.output) + "\n" +
            ResponseTag.ENTER_QUESTION_TAG.__str__() + "\n"
        )
