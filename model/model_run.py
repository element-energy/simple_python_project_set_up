"""
This is the file that contains the control function for the model, responsible for the running of it. Keep this as
    simple and short as possible, showing the various high level steps that the model goes through
    E.g.  In this toy problem the major steps are just:
        - capitalising a constant string
        - Logging it to the console
"""
import logging

from model.constants.globals import GREETING_LINE
from model.string_operations import capitalise_words


def model_run():
    """Capitalise and log whatever is stored in a constant"""
    capitalised_line = capitalise_words(GREETING_LINE)
    logging.info(capitalised_line)
