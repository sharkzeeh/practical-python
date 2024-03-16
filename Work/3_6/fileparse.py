# fileparse.py
#
# Exercise 3.6: Working without Headers

import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        if has_headers and select:
            indices = [headers.index(col) for col in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[col] for col in indices]
            if types:
                row = [func(elem) for func, elem in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


if __name__ == '__main__':
    portfolio = parse_csv(
        '../Data/prices.csv',
        types=[str, float],
        has_headers=False
    )
    print(portfolio)
