# filematch.py
#
# Exercise 6.9: Setting up a more complex pipeline
import types, csv

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    from follow import follow
    lines = follow('../Data/stocklog.csv')          # producer
    assert isinstance(lines, types.GeneratorType)
    # example output
    # "IBM",102.88,"6/11/2007","09:35.51",-0.19,102.87,102.88,102.77,164925

    rows = csv.reader(lines)
    for row in rows:
        print(row)
    # example output
    # ['CAT', '78.03', '6/11/2007', '09:30.43', '-0.49', '78.32', '78.03', '77.99', '175984']
