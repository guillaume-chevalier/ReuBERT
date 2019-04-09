from src.api.response.response_tag import ResponseTag


class QuestionAnsweringPhaseResponse:

    def with_output(self, output):
        return ResponseTag.ANSWER_QUESTION_TAG.__str__().format(output
                                                               ) + "\n" + ResponseTag.ENTER_QUESTION_TAG.__str__()
