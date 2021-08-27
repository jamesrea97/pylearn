"""Module contains an example of the distinction between no thread/thread in Python."""
from concurrent.futures import ThreadPoolExecutor
import time
import logging

from helpers.logging_helper import setup_logging


def long_task(i: int) -> None:
    """Long task."""
    logging.info(f"Starting long task - thread: {i}.")
    time.sleep(2)
    logging.info(f"Ending long task - thread: {i}")


def main() -> None:
    setup_logging()

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(long_task, range(3))

    print('\nThreads can be run concurrently.')


if __name__ == "__main__":
    main()
