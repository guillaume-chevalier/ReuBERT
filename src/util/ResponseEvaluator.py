import stringdist


class ResponseEvaluator:
    def __int__(self):
        pass

    def is_response_close_enough(self, response, expected_response):
        acceptable_levenshtein_threshold = 0.5

        return stringdist.levenshtein(response, expected_response) / 33 < acceptable_levenshtein_threshold
