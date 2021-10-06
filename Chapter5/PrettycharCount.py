from pprint import pprint
mensagem = 'Vini'
count = {}

for char in mensagem:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint(count)