from src.api.response.response_tag import ResponseTag


class InitiatingInteractionResponse:

    def __str__(self):
        return ResponseTag.GREETING_TAG.__str__() + "\n" + ResponseTag.ENTER_INFORMATION_TAG.__str__()
