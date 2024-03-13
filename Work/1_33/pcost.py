# pcost.py
#
# Exercise 1.33: Reading from the command line
import csv, sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as fh:
        csv_rows = csv.reader(fh)
        _headers = next(csv_rows)
        for line in csv_rows:
            share_name = line[0]
            try:
                n_shares = int(line[1])
            except ValueError as e:
                print(f'Value is missing for share {share_name}')
                continue
            try:
                price = float(line[2])
            except ValueError as e:
                print(f'Price is missing for share {share_name}')
                continue
            total_cost += n_shares * price
    return total_cost

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../Data/missing.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost: {cost:.2f}')
