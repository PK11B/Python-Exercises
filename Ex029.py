# Escreva um programa que leia a velocidade de um carro.
# 
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade do carro em Km/h: '))
if vel > 80:
    print('Você excedeu os limites de velocidade!')
    multa = (vel - 80) * 7
    print('Sua multa custará R${:.2f}'.format(multa))
else:
    print('Você está dentro dos limites de velocidade!')
print('Tenha um vom dia')