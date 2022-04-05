# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 por Km para viagens mais longas.

d = float(input('Digite a distância que será percorrida na viagem, em Km: '))

if d <= 200:
    print('Você pagará R${:.2f} pela viagem'.format(d * 0.50))
else:
    print('Você pagará R${:.2f} pela viagem'.format(d * 0.45))

# preço = d * 0.50 if d <= 200 else d * 0.45
