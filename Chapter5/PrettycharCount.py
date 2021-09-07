from pprint import pprint
mensagem = 'Hoje eu vou estudar, andar de bicicleta e me divertir bastante.'
count = {}

for char in mensagem:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint(count)