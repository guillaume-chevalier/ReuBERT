from src.api.response.response_tag import ResponseTag


class QuestionAnsweringPhaseResponse:

    def __init__(self):
        self.output = ""

    def with_output(self, output):
        self.output = output
        return self

    def print(self):
        print("\n" + ResponseTag.ANSWER_QUESTION_TAG.__str__().format(self.output), end="\n")
        print(ResponseTag.ENTER_QUESTION_TAG.__str__(), end="\n")
