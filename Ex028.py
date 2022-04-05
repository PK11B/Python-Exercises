# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# adivinhar qual foi o número escolhido pelo computador
# 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador escolher um número inteiro aleatório entre 0 e 5
print('-=-' * 20)
print('O computador está pensando em um número entre 0 e 5...')
print('-=-' * 20)
jogador = int(input('Tente acertar o número que o computador escolheu: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('VOCÊ VENCEU! O número que o computador escolheu foi: {}'.format(computador))
else:
    print('VOCÊ PERDEU! O número que o computador escolheu foi {}'.format(computador))