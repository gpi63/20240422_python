"""
from typing import Callable


def wrapper(fn: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("Inside of inner")
        return fn(*args, **kwargs)

    return inner


def do_it(a, b) -> int:
    print("in DO IT now")
    return a + b


wrapped_do_it = wrapper(do_it)
print(wrapped_do_it(1, 2))


"""

from typing import Callable


def wrapper(fn: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("Inside of inner")
        return fn(*args, **kwargs)

    return inner


@wrapper
def do_it(a, b) -> int:
    print("in DO IT now")
    return a + b


print(do_it(1, 2))
