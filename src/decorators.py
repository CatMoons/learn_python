from fileinput import filename
from functools import wraps


def log(filename):
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            message_start = f"Starting {func_name} with args {args} kwargs {kwargs}"

            if filename:
                with open(filename, "a") as f:
                    f.write(message_start + "\n")
            else:
                print(message_start)

            try:
                result = func(*args, **kwargs)
                message_successfully = f"{func_name} Successful"
                message_end = f"Finished {func_name} with args {args} kwargs {kwargs}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message_successfully + "\n")
                        f.write(message_end + "\n")
                else:
                    print(message_successfully)
                    print(message_end)

                return result

            except Exception as e:
                message_end = f"Finished {func_name} with args {args} kwargs {kwargs}"
                message_error = f"ERROR: {e}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message_error + "\n")
                        f.write(message_end + "\n")
                else:
                    print(message_error)
                    print(message_end)

        return wrapper

    return decorator

@log(filename=None)
def divide(x, y):
    return x + y

divide(1, 2)