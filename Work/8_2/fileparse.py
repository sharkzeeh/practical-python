# fileparse.py
#
# Exercise 8.2: Adding logging to a module

import csv
import logging

# logging.basicConfig()
# log = logging.getLogger(__name__)
# log.setLevel(logging.WARN)

logging.basicConfig(
    filename='app.log',    # Name of the log file (omit to use stderr)
    filemode='w',          # File mode (use 'a' to append)
    level=logging.WARNING  # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
log = logging.getLogger(__name__)
log.setLevel(logging.WARN)


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
                    log.warning(f"Row {i_row:d}: Couldn't convert {row}")  # f-string or format string
                    log.debug("Row %d: Reason %s", i_row, e)
                continue
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records


if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('../Data/missing.csv', silence_errors=False)
