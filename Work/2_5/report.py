# report.py
#
# Exercise 2.5: List of Dictionaries
import csv, sys, pprint

printer = pprint.PrettyPrinter()

def read_portfolio(filename):
    portfolio = []
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        _headers = next(csv_rows)
        for row in csv_rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/portfolio.csv'


    portfolio = read_portfolio(filename)
    printer.pprint(portfolio)
