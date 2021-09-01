name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print("You're not Alice, kiddo.")
elif age > 2000: #Will execute properly once this condition is met
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, grandma.')

