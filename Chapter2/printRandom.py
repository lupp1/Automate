import random

# prints a random number 5 times, i starts at 0
i = 0
while i < 5:
    print(random.randint(1, 20))
    i += 1
# can also use it as
print('Using "for" loop:')
for i in range(5):
    print(random.randint(1, 20))
