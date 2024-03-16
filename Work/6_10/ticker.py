# ticker.py
#
# Exercise 6.10: Making more pipeline components (Part 1)

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_colums(rows, [0, 1, 4])
    return rows

def select_colums(rows, indices=None):
    for row in rows:
        if indices:
            select = [row[idx] for idx in indices]
            yield select
        else:
            yield row


if __name__ == '__main__':
    lines = follow('../Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

    # example output
    # ['JNJ', '62.09', '-0.04']
