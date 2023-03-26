nome = str(input('Nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('{} sua média foi {}. Reprovado!'.format(nome, media))
elif media <7:
    print('{} sua média foi {}. Recuperação!'.format(nome, media))
else:
    print('{} sua média foi {}. Aprovado!'.format(nome, media))