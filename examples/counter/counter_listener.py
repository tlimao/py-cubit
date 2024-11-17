
import threading
import time
from pycubit.cubit import CubitListener

class CounterListener(CubitListener[int]):

    def __init__(self):
        self._stop_event = threading.Event()

    def on_state_change(self, new_state: int):
        """
        Callback to handle state changes.
        """
        print(f"[Listener] State updated: {new_state}")

    def run(self):
        """
        Continuously listens for state changes.
        """
        print("[Listener] Thread started.")
        while not self._stop_event.is_set():
            time.sleep(0.1)  # Simulate idle work

        print("[Listener] Thread stopped.")

    def stop(self):
        """
        Signals the thread to stop.
        """
        self._stop_event.set()