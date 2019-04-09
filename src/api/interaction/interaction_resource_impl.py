import time

from src.api.interaction.waiting_animation_thread import WaitingAnimationThread
from src.api.interaction.interaction_resource import InteractionResource


# TODO: finish this class
from src.api.response.ending_interaction_response import EndingInteractionResponse
from src.api.response.information_phase_response import InformationPhaseResponse
from src.api.response.initiating_interaction_response import InitiatingInteractionResponse
from src.api.response.question_answering_phase_response import QuestionAnsweringPhaseResponse
from src.api.response.switching_to_question_answering_phase_response import SwitchingToQuestionAnsweringPhaseResponse


class InteractionResourceImpl(InteractionResource):
    FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION = \
        "ReuBERT[greeting]:~$ Welcome! What would you like to talk about?"
    RECEIVING_STATEMENT_INPUT_AREA_BEGIN = \
        "You[enter information]:~$ "
    RECEIVING_STATEMENT_BERT_RESPONSE = \
        "ReuBERT[gather information]:~$ {}"
    RECEIVING_QUESTION_INPUT_AREA_BEGIN = \
        "You[enter question]:~$ "
    RECEIVING_QUESTION_BERT_RESPONSE = \
        "ReuBERT[answer question]:~$ {}"

    def execute(self):
        # print(InteractionResourceImpl.FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION)
        # do_continue = True
        #
        # next_phase_number = 1
        # # next_phase_number = 0
        #
        # while do_continue:
        #     time.sleep(0.5)
        #
        #     user_input_str = self._obtain_user_input(next_phase_number)
        #     next_phase_number, do_continue = self._print_bert_answer(next_phase_number, user_input_str)
        print(InitiatingInteractionResponse())
        while True:
            user_input = input()
            reubert_output = self.interaction_service.process_input_text(user_input)
            print(InformationPhaseResponse().with_output(reubert_output))



    def _obtain_user_input(self, next_phase_number):
        if next_phase_number == 0:
            print(InteractionResourceImpl.RECEIVING_STATEMENT_INPUT_AREA_BEGIN, end="")
        elif next_phase_number == 1:
            print(InteractionResourceImpl.RECEIVING_QUESTION_INPUT_AREA_BEGIN, end="")

        user_input_str = input()
        return user_input_str

    def _print_bert_answer(self, next_phase_number, user_input: str):
        if next_phase_number == 1:
            waiting_animation_thread = WaitingAnimationThread()
            waiting_animation_thread.start()

        time.sleep(2)
        robot_response_str = "Answer here."
        do_continue = True

        #do_continue, next_phase_number, robot_response_str = self.interaction_service.process_input_text(user_input)

        if next_phase_number == 1:
            waiting_animation_thread.join()
            print(InteractionResourceImpl.RECEIVING_STATEMENT_BERT_RESPONSE.format(robot_response_str))
        else:
            print(InteractionResourceImpl.RECEIVING_QUESTION_BERT_RESPONSE.format(robot_response_str))
        return next_phase_number, do_continue
