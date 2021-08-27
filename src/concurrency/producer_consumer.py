"""Module contains an Event & Queues multi-threading example through Producer/Consumer."""
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import logging
import random
from threading import Event

from helpers.logging_helper import setup_logging


def producer(queue: Queue, event: Event):
    """Example of a producer - receives requests and publishes them to the queue."""
    while not event.is_set():
        message = random.randint(1, 101)

        logging.info(f"Publishing message: {message} - Queue size: {queue.qsize()}.")
        queue.put(message)
        logging.info(f"Published message {message} - Queue size: {queue.qsize()}.")

    logging.info("No more messages to produce.")


def consumer(queue: Queue, event: Event) -> None:
    """Exampleof a consumer - reads messages from the queue (published by producer). """
    while not (event.is_set() and queue.empty()):
        message = queue.get()
        logging.info(f"Consumed message:{message} - Queue size: {queue.qsize()}.")

    logging.info("No more messages to be consume.")


def main():
    setup_logging()

    pipeline = Queue(maxsize=3)
    event = Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        logging.info("Starting to send messages to producer.")

        executor.submit(producer, pipeline, event)  # listens on changes of state of event
        executor.submit(consumer, pipeline, event)  # listens on changes of state of event

        event.set()
        logging.info("Stopping to send messages to producer.")


if __name__ == "__main__":
    main()
