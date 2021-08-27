"""Module contains setup logging logic"""
import logging


def setup_logging() -> None:
    """Sets up logging."""
    logging.basicConfig(format="%(asctime)s: %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
