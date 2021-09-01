myPets = ['Chico', 'Francisco', 'Lucas', 'Azazel']
name = input('Enter a pet name: ')
if name not in myPets:
    print('I do not have a pet named {}'.format(name))
else:
    print('I have a pet named {}'.format(name))
