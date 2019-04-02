class UserInputQuestionPair:

    def __init__(self, user_inputs, question):
        self.dict = {"user_input": self._join_user_inputs(user_inputs), "question": question}

    def get_user_input(self):
        return self.dict["user_input"]

    def get_question(self):
        return self.dict["question"]

    def _join_user_inputs(self, user_inputs):
        return "".join(user_inputs)
