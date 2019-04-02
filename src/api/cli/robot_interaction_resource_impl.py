import time

from src.api.cli.waiting_animation_thread import WaitingAnimationThread
from src.api.robot_interaction_resource_interface import RobotInteractionResourceInterface


class CLIRobotInteractionResourceImpl(RobotInteractionResourceInterface):
    FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION = \
        "ReuBERT[greeting]:~$ Welcome! What would you like to talk about?"
    PHASE_1_INPUT_AREA_BEGIN = \
        "You[enter information]:~$ "
    PHASE_2_INPUT_AREA_BEGIN = \
        "You[enter question]:~$ "
    PHASE_1_BERT_RESPONSE = \
        "ReuBERT[gather information]:~$ {}"
    PHASE_2_BERT_RESPONSE = \
        "ReuBERT[answer question]:~$ {}"

    def execute(self):
        # TODO: Note: a few edits are needed for this code to manage the user going idle when asking him something.

        print(CLIRobotInteractionResourceImpl.FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION)
        do_continue = True

        next_phase_number = 1
        # next_phase_number = 0  # TODO: start at 0 as it should..
        while do_continue:
            time.sleep(0.5)
            if next_phase_number == 0:
                print(CLIRobotInteractionResourceImpl.PHASE_1_INPUT_AREA_BEGIN, end="")
            elif next_phase_number == 1:
                print(CLIRobotInteractionResourceImpl.PHASE_2_INPUT_AREA_BEGIN, end="")
            user_input_str = input()

            if next_phase_number == 1:
                wa = WaitingAnimationThread()
                wa.start()

            time.sleep(2)  # TODO: uncomment line below and remove sleep and start at next_phase_number = 0, not 1.
            robot_response_str = "Answer here."
            # do_continue, next_phase_number, robot_response_str = self.interaction_service.process_input_text(
            #     user_input_str
            # )

            if next_phase_number == 1:
                wa.join()
                print(CLIRobotInteractionResourceImpl.PHASE_2_BERT_RESPONSE.format(robot_response_str))
            else:
                print(CLIRobotInteractionResourceImpl.PHASE_1_BERT_RESPONSE.format(robot_response_str))
