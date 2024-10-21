from src.decorators import log
import pytest


@log(filename="log.txt")
def my_log_without_err(x, y):
    return x + y


@log(filename="log.txt")
def my_log_with_err(x, y):
    raise Exception(y)


@log(filename=None)
def divide(x, y):
    return x + y


def test_log_to_console(capsys):
    divide(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "Starting divide with args (1, 2) kwargs {}\nFinished divide with args (1, 2) kwargs {}\n"


def test_log_to_console_with_err(capsys):
    divide(1, "2")

    captured = capsys.readouterr()
    assert (
        captured.out
        == "Starting divide with args (1, '2') kwargs {}\nERROR: unsupported operand type(s) for +: 'int' and 'str'\n"
    )
