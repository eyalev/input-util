
from input_util import I


def test_to_json_string():
    assert I({}).to_json_string() == "{}"


def test_is_url():
    assert I("example.com").is_url
    assert I("example.com j").is_url is False


def test_is_dict():
    assert I({}).is_dict
    assert I({'one': 'one-value'}).is_dict


def test_line_count_with_extra_new_line():

    text = """\
one
two
three
"""

    line_count = I(text).line_count_with_text

    assert line_count == 3


def test_line_count():

    text = """\
one
two
three\
"""

    line_count = I(text).line_count_with_text

    assert line_count == 3

