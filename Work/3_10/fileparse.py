# fileparse.py
#
# Exercise 3.8 - 3.10: Exceptions
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []
        if has_headers and select:
            indices = [headers.index(col) for col in select]
            headers = select
        else:
            indices = []
        records = []
        for i_row, row in enumerate(rows, start=1):
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[col] for col in indices]
            if types:
                try:
                    row = [func(elem) for func, elem in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i_row}: Couldn\'t convert {row}')
                        print(f'Row {i_row}: Reason {e}')
                    continue
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


if __name__ == '__main__':
    portfolio = parse_csv(
        '../Data/missing.csv',
        types=[str, int, float],
        silence_errors=False
    )
    print(portfolio)