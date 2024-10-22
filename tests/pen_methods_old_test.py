# Pen class methods parametrized tests for pytest (old version)
import pytest
from pen_file import Pen


@pytest.mark.parametrize(
    "ink_container_value, size_letter, color",
    [
        (1000, 1.0, 'red'),
        (500, 2.0, 'green'),
        (300, 0.5, 'blue'),
        (0, 1.0, 'black'),

    ]
)
def test_initial_state(ink_container_value, size_letter, color):
    """Test initial state of the pen"""
    pen = Pen(ink_container_value=ink_container_value, size_letter=size_letter, color=color)
    assert pen.ink_container_value == ink_container_value
    assert pen.size_letter == size_letter
    assert pen.color == color


@pytest.mark.parametrize(
    "ink_container_value, size_letter, word, expected_result, expected_ink_left",
    [
        (10, 1.0, "hello", "hello", 5),
        (3, 1.0, "hello", "hel", 0),
        (5, 2.0, "test", "te", 1),
        (0, 1.0, "pen", "", 0),
    ]
)
@pytest.mark.slow
def test_write(ink_container_value, size_letter, word, expected_result, expected_ink_left):
    """Test pen how it writes"""
    pen = Pen(ink_container_value=ink_container_value, size_letter=size_letter)
    result = pen.write(word)
    assert result == expected_result
    assert pen.ink_container_value == expected_ink_left


@pytest.mark.parametrize(
    "ink_container_value, expected_state",
    [
        (5, True),
        (0, False),
        (50, True),
        (100, True),
    ]
)
@pytest.mark.slow
def test_check_pen_state(ink_container_value, expected_state):
    """Test pen state"""
    pen = Pen(ink_container_value=ink_container_value)
    assert pen.check_pen_state() == expected_state


@pytest.mark.parametrize(
    "color, expected_color",
    [
        ('red', 'red'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('black', 'black'),
        ('white', 'white')
    ]
)
@pytest.mark.slow
def test_get_color(color, expected_color):
    """Test get color"""
    pen = Pen(color=color)
    assert pen.get_color() == expected_color
