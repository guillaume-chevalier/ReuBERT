from src.api.response.response_tag import ResponseTag


class InformationPhaseResponse:

    def with_output(self, output):
        return ResponseTag.GATHER_INFORMATION_TAG.__str__().format(output) + "\n" + ResponseTag.ENTER_INFORMATION_TAG.__str__()