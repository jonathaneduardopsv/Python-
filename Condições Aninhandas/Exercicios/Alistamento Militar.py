nome = str(input('Qual seu nome? '))
nascimento = int(input('Qual ano você nasceu? '))
alistamento = 2022 - nascimento
if alistamento < 18:
    faltam = 18 - alistamento
    print('Faltam {} anos para seu alistamento militar!'.format(faltam))
elif alistamento > 18:
    passou = alistamento - 18
    print('Já deveria ter se alistado, está atrasado em {} anos!'.format(passou))
else:
    print('Parabéns! Este é o ano do seu alistamento militar!')
