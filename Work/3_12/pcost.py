# pcost.py
#
# Exersice 3.14: Using more library imports
import fileparse

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    portfolio = fileparse.parse_csv(
        filename,
        has_headers=True,
        select=['shares', 'price'],
        types=[int, float],silence_errors=False
    )
    for stock in portfolio:
        shares = stock['shares']
        price = stock['price']
        total_cost += shares * price
    return total_cost


if __name__ == '__main__':
    cost = portfolio_cost('../Data/portfolio.csv')
    print(cost)
