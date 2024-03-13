# pcost.py
#
# Exercise 1.27: Reading a data file
with open('../Data/portfolio.csv') as fh:
    _headers = next(fh)
    total_cost = 0
    for line in fh:
        line = line.split(',')
        n_shares = int(line[1])
        price = float(line[2])
        total_cost += n_shares * price
print(f'Total cost: {total_cost:.2f}')
