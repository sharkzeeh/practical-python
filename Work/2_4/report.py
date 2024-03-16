# report.py
#
# Exercise 2.4: A list of tuples

import csv, sys

def read_portfolio(filename):
    portfolio = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        _headers = next(csv_rows)
        for row in csv_rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/portfolio.csv'


    portfolio = read_portfolio(filename)
    print(portfolio)
