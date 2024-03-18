# Reading: 7.5 Decorated Methods

# Class methods are most often used as
# a tool for defining alternate constructors.

import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        print(cls)
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # And used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

    def __repr__(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year:d}'

class NewDate(Date):
    ...


if __name__ == '__main__':
    d = Date.today()
    print('Date instance:', d, '\n')
    d2 = NewDate.today()
    print('NewDate instance:', d2)
