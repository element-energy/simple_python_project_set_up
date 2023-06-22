"""Utility functions for the model"""
import logging
import os
from pathlib import Path
from typing import List, Optional


def logging_set_up(log_file_path: Optional[Path] = None):
    """
    Set up the logging, for the run

    :param log_file_path: path to the log file
    """
    handlers: List[logging.Handler] = [logging.StreamHandler()]
    if log_file_path:
        if not os.path.exists(log_file_path.parent):
            log_file_path.parent.mkdir(parents=True)
        handlers += [logging.FileHandler(log_file_path)]
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
    )
