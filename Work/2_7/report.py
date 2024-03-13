# report.py
#
# Exercise 2.7: Finding out if you can retire
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


def portfolio_cost(portfolio, prices):
    total_cost, total_value, total_diff = 0.0, 0.0, 0.0
    for holding in portfolio:
        share_name = holding['name']
        n_shares = holding['shares']
        old_price = holding['price']
        new_price = prices[share_name]
        total_cost += n_shares * old_price
        total_value += n_shares * new_price
        total_diff += (new_price - old_price) * n_shares
    return {
        'total_cost': total_cost, 
        'total_value': total_value, 
        'diff': total_diff
    }


if __name__ == '__main__':
    fn_portfolio = '../Data/portfolio.csv'
    fn_prices = '../Data/prices.csv'

    portfolio = read_portfolio(fn_portfolio)
    prices = read_prices(fn_prices)

    report = portfolio_cost(portfolio, prices)
    printer.pprint(report)
