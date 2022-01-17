data = [['apples', 'bananas', 'oranges', 'mango'], ['John', 'Hobart', 'William', 'Gustavo'],
        ['cats', 'dogs', 'birds', 'elephant'],]
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for y in range(int(len(tableData[0]))):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(5, ' '), end=' ')
        print('\t')
printTable(data)

