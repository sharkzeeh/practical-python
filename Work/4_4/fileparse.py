# fileparse.py
#
# Exercise 3.17: From filenames to file-like objects
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if isinstance(lines, str):
        raise RuntimeError('Pass a file-like object, not string')

    if not has_headers and select:
        raise RuntimeError('Select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

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
    import gzip

    with gzip.open('../Data/portfolio.csv.gz', 'rt') as file:
        portfolio = parse_csv(file, types=[str, int, float])
    print(portfolio)

    ## RuntimeError
    # parse_csv('../Data/portfolio.csv', types=[str,int,float]))