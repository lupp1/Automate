def printPic(itemsDict, lWidth, rWidth):
    print('Picnic items'.center(lWidth + rWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(lWidth, '.') + str(v).rjust(rWidth))
picItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPic(picItems, 13, 13)
printPic(picItems, 13, 13)
