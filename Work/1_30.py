# pcost.py
#
# Exercise 1.30: Turning a script into a function
def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as fh:
        _headers = next(fh)
        for line in fh:
            line = line.split(',')
            n_shares = int(line[1])
            price = float(line[2])
            total_cost += n_shares * price
    return total_cost

if __name__ == '__main__':
    cost = portfolio_cost('./Data/portfolio.csv')
    print(f'Total cost: {cost:.2f}')