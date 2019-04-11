from src.api.response.response import Response
from src.api.response.response_tag import ResponseTag


class EndingInteractionResponse(Response):

    def print(self):
        print("\n" + ResponseTag.GOODBYE_TAG.__str__().format(self.output) + "\n")
