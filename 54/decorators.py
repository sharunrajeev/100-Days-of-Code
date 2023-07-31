# Python Decorator

from time import time
from time import sleep


def speed_calc_decorator(func):
    def wrapper():
        start_time = time()
        func()
        print(f"{func.__name__} run speed: {time() - start_time}")

    return wrapper()


@speed_calc_decorator
def fast_function():
    sleep(1)


@speed_calc_decorator
def slow_function():
    sleep(10)
