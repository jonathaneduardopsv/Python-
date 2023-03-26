print('Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5')
print('Depois peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.')
print('O programa deverá escrever na tela se o usuário venceu ou perdeu.')
print('')
from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(5)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))