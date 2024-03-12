# report.py
#
# Exercise 3.15 - 3.16: main function
import fileparse_3_12 as fileparse
import sys

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))

def make_report_data(portfolio,prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio,prices)

    # Print it out
    print_report(report)

# Main function
def main(argv):
    if len(argv) != 3:
        print('Pass portfolio and prices filename')
        sys.exit(1)
    portfolio_report(*argv[1:])


if __name__ == '__main__':
    # 1
    main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])

    # 2 cmd line
    ## $ python3 report.py Data/portfolio.csv Data/prices.csv
    # main(sys.argv)
