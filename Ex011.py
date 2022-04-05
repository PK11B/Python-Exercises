# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
import math
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
a = (altura*largura)
tinta = a / 2
print('A área da parede será {} m² e você precisará de {} litros de tinta para pintá-la'.format(a, tinta))