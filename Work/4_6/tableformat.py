# tableformat.py
#
# Exercise 4.6: Using Inheritance to Produce Different Output

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
