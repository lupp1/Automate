import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
guess = {}
i = {}
for i in range(1, 7):
    print('Take a guess, you have 6 chances:')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break

if guess == secretNumber:
    print(f'Congrats! You guessed my number in {str(i)} guesses')