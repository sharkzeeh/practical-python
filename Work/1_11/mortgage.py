# mortgage.py
#
# Exercise 1.11: Bonus

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
cur_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    cur_month += 1
    principal = principal * (1 + rate / 12)
    principal -= payment
    total_paid += payment
    if cur_month >= extra_payment_start_month and cur_month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    ### START CODE HERE
    if principal < 0:
        overpay = abs(principal)
        total_paid -= overpay
        principal = 0
    ### END CODE
    print(f'{cur_month:<5} {total_paid:<10.2f} {principal:>10.2f}')


print('Total paid', round(total_paid, 2))
print('Months', cur_month)
