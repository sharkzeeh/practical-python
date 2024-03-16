# filematch.py
#
# Exercise 6.4: A Simple Generator

# The idea that you can hide a bunch of
# custom processing in a function and use it to feed a for-loop

def filematch(filename, substr):
    with open(filename) as fh:
        for line in fh:
            if substr in line:
                yield line


if __name__ == '__main__':
    with open('../Data/portfolio.csv') as fh:
        for line in fh:
            print(line, end='')
    print('\nLines with IBM')
    for line in filematch('../Data/portfolio.csv', 'IBM'):
        print(line, end='')
