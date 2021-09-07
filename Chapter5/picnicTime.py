picnic = {'Gustavo': {'maçãs': 5, 'pretzels': 12},
          'João': {'sanduíche': 3, 'maçãs': 2},
          'Felipe': {'copos': 3, 'tortas': 1}}
def totalBrought(convidados, item):
    numBrought = 0
    for i, j in convidados.items():
        numBrought = numBrought + j.get(item, 0)
    return numBrought
def guestsBrought()
print(f'''Total de coisas para o piquinique:
    - Maçãs: {str(totalBrought(picnic, "maçãs"))}
    - Copos: {str(totalBrought(picnic, "copos"))}
    - Bolos: {str(totalBrought(picnic, "bolos"))}
    - Sanduíches: {str(totalBrought(picnic, "sanduíche"))}
    - Tortas: {str(totalBrought(picnic, "tortas"))}''')
