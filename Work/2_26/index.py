# index.py
#
# Exercise 2.26: The Big Picture
import csv, sys, pprint

def read_index(filename):
    '''Returns portfolio with type conversion'''
    invest_index = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        headers = next(csv_rows)
        types = [str, float, str, str, float, float, float, float, int]
        invest_index = [{
            colname:func(val)
            for colname, val, func
            in zip(headers, row, types)
        } for row in csv_rows]
    return invest_index


if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/dowstocks.csv'
    invest_index = read_index(filename)
    printer = pprint.PrettyPrinter(indent=4)
    printer.pprint(invest_index)
