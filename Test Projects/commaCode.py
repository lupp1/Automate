def commafunc(listValue):
    for i in range(len(listValue) - 2):
        print(listValue[i], end=', ')
    print(f'{listValue[-2]} and {listValue[-1]}')

def generateList():
    spam = []
    n = int(input('Enter the number of elements for the list: '))
    for i in range(0, n):
        element = input(f'Type element number {i}: ')
        spam.append(element)
    return spam
spam = generateList()
commafunc(spam)
