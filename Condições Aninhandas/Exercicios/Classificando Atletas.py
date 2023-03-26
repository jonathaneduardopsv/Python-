nome = str(input('Qual o seu nome? '))
nascimento = int(input('Qual ano você nasceu? '))
idade = 2022 - nascimento
if idade <= 9:
    print('{}, Você é um atleta Mirim.'. format(nome))
elif idade <= 14:
    print('{}, você é um atleta Infantil.'.format(nome))
elif idade <= 19:
    print('{}, você é um atleta Júnior.'.format(nome))
elif idade <= 25:
    print('{}, você é um atleta Sênior.'.format(nome))
else:
    print('{}, você é um atleta Master.'.format(nome))

