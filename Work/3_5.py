# fileparse.py
#
# Exercise 3.5: Performing Type Conversion
import csv

def parse_csv(filename, select=None, types=[str, int, float]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select:
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
            record = dict(zip(headers, row))
            records.append(record)

    return records


if __name__ == '__main__':
    portfolio = parse_csv(
        'Data/portfolio.csv',
        select=['name', 'shares'],
        types=[str, int]
    )
    print(portfolio)