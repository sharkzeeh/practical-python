# report.py
#
# Exercise 2.20: Sequence Reductions
import csv, sys, pprint

def read_portfolio(filename):
    '''Returns portfolio without type conversion'''
    portfolio = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        headers = next(csv_rows)
        select = ['name', 'shares', 'price']
        indices = [headers.index(sel) for sel in select]
        portfolio = [
            {
                colname:row[index]
                for colname, index
                in zip(select, indices)
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
    cost = sum(
        [int(stock['shares']) * float(stock['price']) for stock in portfolio]
    )
    print(f'{cost:.2f}')
