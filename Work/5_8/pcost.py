# pcost.py

import sys
import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    total_cost = sum((s.cost for s in portfolio))
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
