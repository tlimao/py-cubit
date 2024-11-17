import threading
import time
from counter_cubit import CounterCubit
from counter_listener import CounterListener


if __name__ == "__main__":
    # Create the CounterCubit
    counter_cubit: CounterCubit = CounterCubit()

    # Create and attach the listener
    counter_listener: CounterListener = CounterListener()
    counter_cubit.add_listener(counter_listener)

    # Start the listener in a daemon thread
    listener_thread = threading.Thread(target=counter_listener.run, daemon=True)
    listener_thread.start()

    # Interact with the Cubit
    try:
        for _ in range(5):
            counter_cubit.increment()
            time.sleep(1)  # Simulate work in the main thread

        for _ in range(3):
            counter_cubit.decrement()
            time.sleep(1)

    finally:
        # Stop the listener and exit
        counter_listener.stop()
        listener_thread.join()  # Ensure the thread stops cleanly
        print("[Main] Application shutting down.")
    
    