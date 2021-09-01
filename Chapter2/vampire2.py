name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print("You're not Alice, kiddo.")
elif age > 100: #Will execute once this condition is met
    print('You are not Alice, grandma.')
elif age > 2000: #This will be skipped. Therefore, it's not logically correct/possible
    print('Unlike you, Alice is not an undead, immortal vampire')

