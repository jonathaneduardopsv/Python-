velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    print('Você foi Multado por excesso de velocidade!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {}'.format(multa))
print('Tenha um bom dia.Dirija com segurança!')