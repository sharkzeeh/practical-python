# timethis.py
#
# Exercise 7.10: A decorator for timing

import time, functools

def timethis(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}, {func.__name__}, {end-start:f}')
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(10000000)
