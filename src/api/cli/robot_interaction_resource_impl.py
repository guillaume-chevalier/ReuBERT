import abc
import os
import sys
import time

from src.api.robot_interaction_resource_interface import RobotInteractionResourceInterface


class CLIRobotInteractionResourceImpl(RobotInteractionResourceInterface):
    FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION = "Welcome! What would you like to talk about?\n > "

    def execute(self):
        # TODO: Note: a few edits are needed for this code to manage the user going idle when asking him something.

        print(CLIRobotInteractionResourceImpl.FIRST_WELCOME_MESSAGE_BEFORE_INTERACTION, end="")
        do_continue = True

        next_phase_number = 0
        while (do_continue):
            user_input_str = input()

            if next_phase_number == 1:
                self._wait(
                )  # TODO: wait "until" the answer from the UserRobotInteractionService arrives, then show answer

            do_continue, next_phase_number, robot_response_str = UserRobotInteractionService.receiveUserText(
                user_input_str
            )

            print(robot_response_str)

    def _wait(self):
        # This method is inspired from: https://gist.github.com/guillaume-chevalier/62afc6b46df18c5e77fb2e51016ba4f3

        _, cols = os.popen('stty size', 'r').read().split()
        cols = int(cols)

        # You can choose or create a different animation pattern:
        # chars = "_.~\"|"
        # chars = "\"`-._,-'"
        # chars = """|/-.-\\|/-'-\\"""
        # chars = """|/-\\|/-\\"""
        chars = "_,.-'¯    "

        message = "| ReuBERT is reading and understanding text to answer your question. |"
        cols -= len(message)
        half_cols = int(cols / 2)

        for i in range(1000):
            time.sleep(0.07)
            sys.stdout.write(
                "\r" + "".join([chars[(i + j) % len(chars)] for j in range(half_cols)]) + message +
                "".join([chars[(i - j) % len(chars)] for j in range(half_cols)])
            )
            sys.stdout.flush()
