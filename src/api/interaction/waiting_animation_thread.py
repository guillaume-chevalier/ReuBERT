import os
import threading


class WaitingAnimationThread(threading.Thread):
    MESSAGE = ":~$ ReuBERT is reading and understanding text to answer your question. $~:"

    def __init__(self):
        self.stopping_event = threading.Event()
        self.sleep_interval = 0.07
        threading.Thread.__init__(self, name=self.__class__.__name__)

    def run(self):
        all_cols, chars, half_cols = self._get_columns_settings()
        i = 0
        while not self.stopping_event.isSet():
            self._print_animation_frame(chars, half_cols, i)
            i += 1
        self._eraze_animation_on_exit(all_cols)

    def _get_columns_settings(self):
        try:
            _, all_cols = os.popen('stty size', 'r').read().split()
            all_cols = int(all_cols)
        except Exception as e:
            all_cols = 120  # Assumed default terminal size.
        chars = self._get_animation_pattern()
        cols = all_cols - len(WaitingAnimationThread.MESSAGE)
        half_cols = int(cols / 2)
        return all_cols, chars, half_cols

    def _get_animation_pattern(self):
        # You can choose or create a different animation pattern:
        # chars = "_.~\"|"
        # chars = "\"`-._,-'"
        # chars = """|/-.-\\|/-'-\\"""
        # chars = """|/-\\|/-\\"""
        chars = "_,.-'¯    "
        return chars

    def _print_animation_frame(self, chars, half_cols, i):
        animated_ = "\r" + "".join(
            [chars[(i + j) % len(chars)] for j in range(half_cols)]) \
                    + WaitingAnimationThread.MESSAGE + "".join(
            [chars[(i - j) % len(chars)] for j in range(half_cols)])
        print(animated_, end="\r")
        self.stopping_event.wait(self.sleep_interval)

    def _eraze_animation_on_exit(self, all_cols):
        print(" " * all_cols, end="\r")

    def join(self, timeout=None):
        self.stopping_event.set()
        threading.Thread.join(self, timeout=None)
