# Reading: 6.4 More Generators

# Generator Expressions
# Differences with List Comprehensions
    # Does not construct a list
    # Only useful purpose is iteration
    # Once consumed, can't be reused

nums = [1, 2, 3]
b = (2 * x for x in nums)

print(b)
for elem in b:
    print(elem, end= ' ')
print()

# produces no output
for elem in b:
    print(elem, end= ' ')

summ = sum([x*x for x in nums])    # A list comprehension
print(summ)
summ = sum(x*x for x in nums)      # A generator expression
print(summ)

# The main use of generator expressions is in code that performs some
# calculation on a sequence, but only uses the result once. For
# example, strip all comments from a file.

print('\n###')
with open('somefile.txt') as fh:
    lines = (line for line in fh if not line.startswith('#'))
    for i, line in enumerate(lines):
        print(i, line, end='')
