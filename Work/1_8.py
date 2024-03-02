# mortgage.py
#
# Exercise 1.8: Extra payments
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
cur_month = 0
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate / 12)
    principal -= payment
    total_paid += payment
    if cur_month < 12:
        principal -= extra_payment
        total_paid += extra_payment
    cur_month += 1


print('Total paid', round(total_paid, 2))
print('Months', cur_month)
