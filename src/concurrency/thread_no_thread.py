"""Module contains an example of the distinction between no thread/thread in Python."""
import threading
import time
import logging

from helpers.logging_helper import setup_logging


def long_task() -> None:
    """Long task."""
    logging.info("Starting long task.")
    time.sleep(2)
    logging.info("Ending long task")


def without_thread() -> None:
    """Example function without threading."""

    logging.info("Starting program.")

    logging.info("No threading - run method directly.")

    long_task()

    logging.info("Stopping program.")


def with_thread() -> None:
    """Example function with threading."""

    logging.info("Starting program.")

    thread = threading.Thread(target=long_task)

    logging.info("Starting thread.")
    thread.start()

    logging.info("Waiting for thread to finish.")

    logging.info("Stopping program.")


def main() -> None:
    setup_logging()

    logging.info("Without Threading...")
    without_thread()

    print("")
    time.sleep(4)

    logging.info("With Threading...")
    with_thread()

    print('\nThreads allow for tasks to be run concurrently - i.e. whilst other tasks execute.\n'
          'Notice how program must wait for long task to end in no-threading case.\n'
          'Notice how program can execute long task "pseudo-concurrently" with main task.\n'
          '"pseudo-concurrently" since Python does not allow for actual concurrency '
          'due to the GIL (see ./src/threading/NOTES.md for details).')


if __name__ == "__main__":
    main()
