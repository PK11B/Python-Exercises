# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um valor real para eu te mostrar sua porção inteira: '))
print('Você digitou o valor {}, sua porção inteira é {}'.format(n, trunc(n)))