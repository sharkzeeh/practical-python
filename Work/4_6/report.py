# report.py

import fileparse, tableformat
import sys
from stock import Stock

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        dictdata = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])

    return [Stock(d['name'], d['shares'], d['price']) for d in dictdata]

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as f:
        return dict(fileparse.parse_csv(f, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    # formatter = tableformat.TextTableFormatter()
    # formatter = tableformat.CSVTableFormatter()
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

# Main function
def main(argv):
    if len(argv) != 3:
        print('Pass portfolio and prices filename')
        sys.exit(1)
    portfolio_report(*argv[1:])


if __name__ == '__main__':
    # 1
    main(['report.py', '../Data/portfolio.csv', '../Data/prices.csv'])

    # 2 cmd line
    ## $ python3 report.py ../Data/portfolio.csv ../Data/prices.csv
    # main(sys.argv)
