# tableformat.py
#
# Exercise 4.10: An example of using getattr()
# Exercise 4.11: Defining a custom exception

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Output portfolio data in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for elem in rowdata:
            print(f'{elem:>10}', end=' ')
        print()

    # def row(self, rowdata):
    #     for elem in rowdata:
    #         print('%10s %10d %10.2f %10.2f' % elem)

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def wrap_tr(self, s):
        print(f"<tr>{s}</tr>")

    def headings(self, headers):
        headers_formatted = "".join([f'<th>{h}</th>' for h in headers])
        self.wrap_tr(headers_formatted)
    
    def row(self, rowdata):
        row_formatted = "".join([f'<td>{elem}</td>' for elem in rowdata])
        self.wrap_tr(row_formatted)

class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {name}")
    return formatter

def print_table(dictdata, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in dictdata:
        select = {getattr(obj, col) for col in columns if hasattr(obj, col)}
        formatter.row(select)


if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('../Data/portfolio.csv')
    # print(portfolio)

    formatter = TextTableFormatter()
    print_table(portfolio, ['name', 'shares'], formatter)

    create_formatter("xls")
