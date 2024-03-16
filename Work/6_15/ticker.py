# ticker.py
#
# Exercise 6.11: Filtering data
# Exercise 6.12: Putting it all together

from follow import follow
import csv
import typing as t
import report
import tableformat

def parse_stock_data(lines: t.Generator):
    rows = csv.reader(lines)
    rows = select_colums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_colums(rows: t.Generator, indices: t.List):
    return ([row[idx] for idx in indices] for row in rows)

def convert_types(rows: t.Generator, types: t.List):
    return ([func(val) for func, val in zip(types, row)] for row in rows)

def make_dicts(rows: t.Generator, headers: t.List):
    return (dict(zip(headers, row)) for row in rows)

def filter_symbols(rows: t.Generator, names: t.List):
    return (row for row in rows if row['name'] in names)

def ticker(portfile: str, logfile: str, fmt: str = 'txt'):
    formatter = tableformat.create_formatter(fmt)
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:.2f}", f"{row['change']:.2f}"])

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfoliofile logfile fmt')
    ticker(*args[1:])


if __name__ == '__main__':
    ## 6.12
    main(['ticker.py', '../Data/portfolio.csv', '../Data/stocklog.csv', 'txt'])
    
    # import sys
    # main(sys.argv)

    ## 6.11
    # import report
    # portfolio = report.read_portfolio('../Data/portfolio.csv')
    # lines = follow('../Data/stocklog.csv')
    # rows = parse_stock_data(lines)
    # rows = filter_symbols(rows, portfolio)
    # for row in rows:
    #     print(row)
    
    ## example output
    # {'name': 'CAT', 'price': 78.0, 'change': -0.52}

