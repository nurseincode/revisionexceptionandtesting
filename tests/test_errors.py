import pytest

from tests.errors import convert_to_integer

def test_integer():
    assert convert_to_integer(123) == 123

def test_string():
    assert convert_to_integer('123') == 123

# def test_invalid_string():
#     assert convert_to_integer('hello') is None

# def test_float():
#     assert convert_to_integer(12.8) == 12 

def test_word():
    with pytest.raises(ValueError):
        convert_to_integer('hello') 

# def test_float():
#     assert convert_to_integer('12.8') == 12  # Fails





