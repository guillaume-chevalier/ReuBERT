import os
import threading


class WaitingAnimationThread(threading.Thread):
    MESSAGE = ":~$ ReuBERT is reading and understanding text to answer your question. $~:"

    def __init__(self):
        self.stopping_event = threading.Event()
        self.sleep_interval = 0.07
        threading.Thread.__init__(self, name=self.__class__.__name__)

    def run(self):

        try:
            _, all_cols = os.popen('stty size', 'r').read().split()
            all_cols = int(all_cols)
        except Exception as e:
            all_cols = 120  # Assumed default terminal size.

        # You can choose or create a different animation pattern:
        # chars = "_.~\"|"
        # chars = "\"`-._,-'"
        # chars = """|/-.-\\|/-'-\\"""
        # chars = """|/-\\|/-\\"""
        chars = "_,.-'¯    "

        cols = all_cols - len(WaitingAnimationThread.MESSAGE)
        half_cols = int(cols / 2)

        i = 0
        while not self.stopping_event.isSet():
            animated_ = "\r" + "".join(
                [chars[(i + j) % len(chars)] for j in range(half_cols)]) \
                        + WaitingAnimationThread.MESSAGE + "".join(
                [chars[(i - j) % len(chars)] for j in range(half_cols)])
            print(animated_, end="\r")
            i += 1
            self.stopping_event.wait(self.sleep_interval)
        print(" " * all_cols, end="\r")

    def join(self, timeout=None):
        self.stopping_event.set()
        threading.Thread.join(self, timeout=None)
