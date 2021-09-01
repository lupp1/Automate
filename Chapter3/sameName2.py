def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
print(eggs)#the output should be 'global'
spam()
print(eggs) #the output should be 'spam'
