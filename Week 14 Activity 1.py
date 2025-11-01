# EXPLANATION:
# This code demonstrates how a Python decorator works by wrapping
# an existing function with additional behavior—logging in this case.
# The decorator `log_decorator` takes a function as an argument, defines
# an inner function `wrapper()` that prints a message before and after
# the original function is executed, and then returns this wrapper.
# When the decorator is applied using `@log_decorator`, any call to the
# function `add()` is intercepted by `wrapper()`. The arguments and
# return value are printed, effectively adding logging functionality
# without modifying the original `add()` function directly.
# -----------------------------------------------------------

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Example usage
add(3, 5)