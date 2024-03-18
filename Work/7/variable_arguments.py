# Reading: 7.1 Variable Arguments

# This function takes any combination of positional or keyword
# arguments. It is sometimes used when writing wrappers or when you
# want to pass arguments through to another function.

def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    print('Positional arguments:', end=' ')
    for arg in args:
        print(arg, end=' ')
    
    print('\nKeyword arguments:')
    for k, v in kwargs.items():
        print(f'\t{k}: {v}')

# Tuples can be expanded into variable arguments.
numbers = (2,3,4)
f(1, *numbers)            # Same as f(1,2,3,4)

print('#######')
# Dictionaries can also be expanded into keyword arguments.
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}

data = 42
f(data, **options)  # Same as f(data, color='red', delimiter=',', width=400)
