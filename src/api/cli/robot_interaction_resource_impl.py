import abc

from src.api.robot_interaction_resource_interface import RobotInteractionResourceInterface


class CLIRobotInteractionResourceImpl(RobotInteractionResourceInterface):
    FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION = "Welcome! What would you like to talk about?"

    def execute(self):
        # TODO: Note: a few edits are needed for this code to manage the user going idle when asking him something.

        print(CLIRobotInteractionResourceImpl.
              FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION)
        do_continue = True

        while (do_continue):
            user_input_str = input()
        do_continue, robot_response_str = UserRobotInteractionService.receiveUserText(
            user_input_str)
        print(robot_response_str)
