# pcost.py
#
# Exercise 2.16: Using the zip() function
import csv, sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        headers = next(csv_rows)
        for rowno, row in enumerate(csv_rows, start=1):
            try:
                record = dict(zip(headers, row))
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError as e:
                print(f"Row {rowno}: Couldn't convert {row}")
                continue
    return total_cost


if __name__ == '__main__':

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/missing.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost: {cost:.2f}')
