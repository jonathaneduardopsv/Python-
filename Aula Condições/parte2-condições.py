nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('A média do aluno foi {}'.format(media))
if media >= 7:
    print('TOP')
else:
    print('se lascou')