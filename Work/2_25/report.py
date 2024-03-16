# report.py
#
# Exercise 2.25: Making dictionaries

import csv, sys, pprint

def read_portfolio(filename):
    '''Returns portfolio with type conversion'''
    portfolio = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        headers = next(csv_rows)
        select = ['name', 'shares', 'price']
        types = [str, int, float]
        indices = [headers.index(sel) for sel in select]
        portfolio = [
            {
                colname:func(row[index])
                for colname, index, func
                in zip(select, indices, types)
            } for row in csv_rows
        ]
    return portfolio


if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    printer = pprint.PrettyPrinter(indent=4)
    printer.pprint(portfolio)
    cost = sum([stock['shares'] * stock['price'] for stock in portfolio])
    print(f'{cost:.2f}')
