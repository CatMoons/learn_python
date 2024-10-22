from src.decorators import log


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
    """
    Проверяет программу на правильность вывода в консоль с учетом отсутствия ошибки
    """
    divide(1, 2)

    captured = capsys.readouterr()
    assert (
        captured.out == "Starting divide with args (1, 2) kwargs {}\ndivide Successful\n"
        "Finished divide with args (1, 2) kwargs {}\n"
    )


def test_log_to_console_with_err(capsys):
    """
    Проверяет программу на правильность вывода в консоль с учетом наличия ошибки
    """
    divide(1, "2")

    captured = capsys.readouterr()
    assert (
        captured.out
        == "Starting divide with args (1, '2') kwargs {}\nERROR: unsupported operand type(s) for +: 'int' and 'str'\n"
        "Finished divide with args (1, '2') kwargs {}\n"
    )
