# report.py
import csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name': record['name'],
                 'shares': int(record['shares']),
                 'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio: list, prices: dict):
    report = []
    for holding in portfolio:
        share_name = holding['name']
        n_shares = holding['shares']
        old_price = holding['price']
        new_price = prices[share_name]
        stock_report = (
            share_name, n_shares, new_price, new_price - old_price
        )
        report.append(stock_report)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    div = '-' * 10
    print(f'{" ".join([div] * 4)}')
    for stock in report:
        stock = (stock[0], stock[1], '$' + f'{stock[2]:.2f}', stock[3])
        print('{:>10} {:>10d} {:>10} {:>10.2f}'.format(*stock))

def portfolio_report(portfolio_fname, prices_fname):
    portfolio = read_portfolio(portfolio_fname)
    prices = read_prices(prices_fname)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    portfolio_report('../Data/portfolio.csv', '../Data/prices.csv')