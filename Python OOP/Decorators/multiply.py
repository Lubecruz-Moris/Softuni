from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(params):
            return times * function(params)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

