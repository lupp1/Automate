def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')
for i in range (0, 12): #error, can't divide by zero
    print(spam(i))
