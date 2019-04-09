from src.api.response.response_tag import ResponseTag


class EndingInteractionResponse:

    def __str__(self):
        return ResponseTag.GOODBYE_TAG.__str__()