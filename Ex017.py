# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa
from math import hypot
op = float(input('Digite o comprimento do cateto opsoto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hyp = hypot(op, adj)
print('O valor da hipotenusa é {:.2f}'.format(hyp))