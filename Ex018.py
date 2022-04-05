# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
n = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
print('O ângulo escolhido foi {}°\n'
      '\nSeu seno é {:.2f}'
      '\nSeu cosseno é {:.2f}'
      '\nSua tangente é {:.2f}'.format(n, seno, cosseno, tangente))