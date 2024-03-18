# Reading: 7.2 Anonymous Functions and Lambda

# How do we sort a list of dicts?

portfolio = [{'name': 'AA', 'price': 32.2, 'shares': 100},
            {'name': 'IBM', 'price': 91.1, 'shares': 50},
            {'name': 'CAT', 'price': 83.44, 'shares': 150},
            {'name': 'MSFT', 'price': 51.23, 'shares': 200},
            {'name': 'GE', 'price': 40.37, 'shares': 95},
            {'name': 'MSFT', 'price': 65.1, 'shares': 50},
            {'name': 'IBM', 'price': 70.44, 'shares': 100}]

portfolio2 = list(portfolio)

# You can guide the sorting by using a key function. The key
# function is a function that receives the dictionary and returns the
# value of interest for sorting.


# In the above example, the key function is an example of a callback
# function. The sort() method "calls back" to a function you supply.
# Callback functions are often short one-line functions that are only
# used for that one operation. Programmers often ask for a short-cut
# for specifying this extra processing.

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# Using lambda lambda is highly restricted.
# Only a single expression is allowed.
# No statements like if, while, etc.
# Most common use is with functions like sort().

portfolio2.sort(key=lambda s: s['name'])

import pprint
printer = pprint.PrettyPrinter(indent=2)
printer.pprint(portfolio)
print()
printer.pprint(portfolio2)
