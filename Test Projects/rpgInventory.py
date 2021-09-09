#Programa que mostra o total de itens em uma mochila
inventory = {'Flechas': 15, 'Pacote de Aventureiro': 1, 'Corda': 2, 'Adaga': 1,
             'Moedas': 100, 'Poção de vida': 3}
def displayInventory(bagOfStuff):
    print('Seu inventário é: ')
    totalItens = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        totalItens += v
    print(f'O total de itens na mochila é: {totalItens}')
displayInventory(inventory)
