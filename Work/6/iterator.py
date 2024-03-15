# list iterator
obj = [1, 2, 3]

_iter = obj.__iter__()

while True:
    try:
        elem = _iter.__next__()
        print(elem)
    except StopIteration:
        print('All items were exhausted!')
        break

print('\n\n')

# file iterator
f = open('../Data/portfolio.csv')
assert f == iter(f)

line = next(f)
print(line)

line2 = next(f)
print(line2)
