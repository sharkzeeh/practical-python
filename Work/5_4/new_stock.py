# Exercise 5.5: Inheritance

from stock import Stock

class NewStock(Stock):
    def yow(self):
        print('Yow!')


if __name__ == '__main__':
    n = NewStock('ACME', 50, 123.45)
    print(NewStock.__bases__)
    print(NewStock.__mro__)
    for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            print(f'method "cost" was found in {cls}!')
            break