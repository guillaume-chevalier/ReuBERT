from src.api.response.response_tag import ResponseTag


class SwitchingToQuestionAnsweringPhaseResponse:

    def with_output(self, output):
        return ResponseTag.GATHER_INFORMATION_TAG.__str__().format(output
                                                                  ) + "\n" + ResponseTag.ENTER_QUESTION_TAG.__str__()
