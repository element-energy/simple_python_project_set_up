"""
Example run.py file. This should contain an if __name__ == "__main__" statement and should just call a simple
    entry point in the source folder. Ideally this is the only place where the statement
    if __name__ == "__main__" would appear.
"""
from model.model_run import model_run
from model.utils import logging_set_up

if __name__ == "__main__":
    logging_set_up()
    model_run()
