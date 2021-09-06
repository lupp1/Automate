birthdays = {'Gustavo': 'Jan 14', 'João': 'Abr 10', 'Laércio': 'Dez 10'}
while True:
    print(f'Enter a name (blank to quit): ' )
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Updated')