"""
If you are running a daemon thread on you program and that thread raises an exception,
you might not get it in your log file. I made this sketch to find out how to fix that.

Call this script with:
    python sketch_thread_log.py > thread_log.txt

(Yeah, I'm making my own logging statements with prints and redirecting the output to a
file...)

Hope it helps!
"""


import threading
import traceback
from time import sleep
import sys


def main_thread() -> None:
    """Just the main thread"""

    print("main thread began")
    stop_event = threading.Event()
    daemon_thread = threading.Thread(daemon=True, target=daemon_func, args=[stop_event])

    daemon_thread.start()
    sleep(2)
    stop_event.set()
    print("main thread over")


def daemon_func(stop_event: threading.Event) -> None:
    """Function that will be run in the daemon thread"""

    print("daemon thread began")
    while not stop_event.is_set():
        print("daemon thread running")

        # this line makes the loop hang, and the exception is not recorded in the log
        #bad_function()

        # this try/catch catches the exception and prints it in the log; the loop also
        #  does not hang
        try:
            bad_function()
        except Exception:
            print("\n" + "-" * 60)
            print("exception in daemon thread:")
            traceback.print_exc(file=sys.stdout)
            print("-" * 60 + "\n")

        sleep(0.5)
    print("daemon thread over")


def bad_function() -> None:
    """Raises a runtime error"""

    raise RuntimeError("bad function: i warned you, but you didn't listen...")


if __name__ == "__main__":
    main_thread()
