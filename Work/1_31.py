# pcost.py
#
# Exercise 1.31: Error handling
def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as fh:
        _headers = next(fh)
        for line in fh:
            line = line.split(',')
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