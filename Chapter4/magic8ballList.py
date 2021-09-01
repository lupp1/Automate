import random
mensagens = ['É certo de acontecer',
             'É decididamente assim',
             'Sim, definitivamente',
             'Resposta nebulosa, tente novamente',
             'Pergunte mais tarde',
             'Concentre-se e pergunte novamente',
             'Minha resposta é não',
             'Presumo que não seja bom',
             'Bem duvidoso',]
print(mensagens[random.randint(0, len(mensagens) - 1)])
