"""
Example integration test file. The purpose of this test is to run the model blindly and test if it runs end to end.
    For a model you would want to have some dummy input data that essentially does the same sort of testing
"""
import logging

from model.model_run import model_run


def test_full_model_run(caplog):
    """Testing whether the model runs end to end. Calling model run end point.
    Checking if something has been logged"""
    caplog.set_level(logging.INFO)
    model_run()
    assert len(caplog.text) > 0
