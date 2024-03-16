# pcost.py
#
# Exercise 3.18: Fixing existing functions

import fileparse
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    with open(filename) as f:
        portfolio = fileparse.parse_csv(
            f,
            has_headers=True,
            select=['shares', 'price'],
            types=[int, float],silence_errors=False
        )
        for stock in portfolio:
            shares = stock['shares']
            price = stock['price']
            total_cost += shares * price
    return total_cost

# Main function
def main(argv):
    if len(argv) != 2:
        print('Pass portfolio filename')
        sys.exit(1)
    cost = portfolio_cost(*argv[1:])
    print(f'Total cost: {cost:.2f}')

if __name__ == '__main__':
    # 1
    main(['pcost.py', '../Data/portfolio.csv'])

    # 2 cmd line
    ## $ python3 pcost.py ../Data/portfolio.csv
    # main(sys.argv)
