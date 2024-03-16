# ticker.py
#
# Exercise 6.10: Making more pipeline components (Part 2)

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_colums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_colums(rows, indices):
    for row in rows:
        select = [row[idx] for idx in indices]
        yield select

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


if __name__ == '__main__':
    lines = follow('../Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

    # example output
    # {'name': 'CAT', 'price': 78.0, 'change': -0.52}
