# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
# Ex: Digite um número: 1834
# 
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

from math import trunc


num = int(input('Digite um valor entre 0 e 9999: '))
unidade = (num / 1) % 10
dezena = (num / 10) % 10
centena = (num / 100) % 10
milhar = (num / 1000) % 10

print('unidade: {}'.format(trunc(unidade)))
print('dezena: {}'.format(trunc(dezena)))
print('centena: {}'.format(trunc(centena)))
print('milhar: {}'.format(trunc(milhar)))