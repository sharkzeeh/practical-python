# Reading: 7.3 Returning Functions

# Closures
# When an inner function is returned as a result,
# that inner function is known as a closure.

# Essential feature: A closure retains the values of all variables
# needed for the function to run properly later on. Think of a
# closure as a function plus an extra environment that holds the values
# of variables that it depends on.

# Using Closures
# Closure are an essential feature of Python.
# However, their use if often subtle.

# Common applications:
    # Use in callback functions.
    # Delayed evaluation.
    # Decorator functions.

# Code Repetition
# Closures can also be used as technique for avoiding excessive code repetition.
# You can write functions that make code.

def after(seconds, func):
    import time
    time.sleep(seconds)
    func(5)

def greeting(*args):
    print('Hello Guido')

after(3, greeting)
# after executes the supplied function... later.

def add(x, y):
    def do_add(z):
        print(f'Adding {x} + {y} + {z} -> {x+y+z}')
    return do_add

after(3, add(2, 3))
