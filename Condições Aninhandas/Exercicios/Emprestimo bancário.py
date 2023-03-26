print('Bem vindo ao Banco JEPS')
nome = str(input('Qual o seu nome? '))
valorc = float(input('Qual valor da casa que deseja adquirir? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Quantos anos pretende pagar essa casa ? '))
prestacao = valorc / (tempo * 12)
if prestacao <= salario * 30 / 100:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')

