# report.py
#
# Exercise 2.12: Formatting Challenge

import csv, pprint

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


def read_prices(filename):
    prices = {}
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        for row in csv_rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError as e:
                continue
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


if __name__ == '__main__':
    fn_portfolio = '../Data/portfolio.csv'
    fn_prices = '../Data/prices.csv'

    portfolio = read_portfolio(fn_portfolio)
    prices = read_prices(fn_prices)

    report = make_report(portfolio, prices)
    # printer.pprint(report) # Exercise 2.9: Collecting Data

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    div = '-' * 10
    print(f'{" ".join([div] * 4)}')
    for stock in report:
        stock = (stock[0], stock[1], '$' + f'{stock[2]:.2f}', stock[3])
        print('{:>10} {:>10d} {:>10s} {:>10.2f}'.format(*stock))
