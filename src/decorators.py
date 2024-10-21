from fileinput import filename
from functools import wraps


def log(filename):
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
                message_end = f"Finished {func_name} with args {args} kwargs {kwargs}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message_end + "\n")
                else:
                    print(message_end)

                return result

            except Exception as e:
                message_error = f"ERROR: {e}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message_error)
                else:
                    print(message_error)

        return wrapper

    return decorator
