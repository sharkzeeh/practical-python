# report.py
#
# Exercise 2.6: Dictionaries as a container
import csv, sys, pprint

printer = pprint.PrettyPrinter()

def read_prices(filename):
    prices = {}
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        for row in csv_rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError as e:
                print('Empty row!')
    return prices

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '.././Data/prices.csv'

    portfolio = read_prices(filename)
    printer.pprint(portfolio)
