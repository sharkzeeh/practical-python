# pcost.py
#
# Exercise 1.32: Using a library function
import csv

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

cost = portfolio_cost('./Data/missing.csv')
print(f'Total cost: {cost:.2f}')