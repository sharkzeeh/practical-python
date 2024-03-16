# filematch.py
#
# Exercise 6.8: Setting up a simple pipeline
import types

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    from follow import follow
    lines = follow('../Data/stocklog.csv')  # producer
    ibm = filematch(lines, 'IBM')           # processing / consumer
    assert isinstance(lines, types.GeneratorType) and \
            isinstance(ibm, types.GeneratorType)
    for line in ibm:
        print(line) 

    # example output
    # "IBM",102.89,"6/11/2007","09:36.24",-0.18,102.87,102.89,102.77,173483