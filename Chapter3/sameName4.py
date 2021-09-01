#supposed to show an error
def spam():
    print(eggs)
    eggs = 'spam local'
eggs = 'global'
spam()
