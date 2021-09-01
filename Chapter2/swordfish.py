while True:
    print('Who are you?')
    name = input()
    if name != 'Gustavo':  # If name not equal to Gustavo, repeats the loop
        continue
    print("Hello, Gustavo. What's the password?")
    password = input()
    if password == 'swordfish':
        break
print('Access Granted.')
