"""
Example unit test file. Unit tests are testing that the building blocks of the operations are set up properly.
    This means testing that under certain set of input data the correct outputs are generated.
    Unit testing in general enforces a nice and readable code design. Testable code will be sufficiently granular.
"""
from model.string_operations import capitalise_words


def test_capitalise_words():
    """Test capitalise the words in a string"""
    input_string = "ses goes coding"
    expected_output_string = "Ses Goes Coding"
    actual_output_string = capitalise_words(input_string)
    assert actual_output_string == expected_output_string
