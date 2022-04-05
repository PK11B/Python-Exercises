# Crie um programa que leia quanto uma pessoa tem de dinheiro na carteira e mostre quantos dólares ela pode comprar (dólar hoje = 5.14)
reais = float(input('Digite um valor em reais: R$ '))
dólar = reais / 5.14
print('Com R$ {:.2f} você tem US$ {:.2f}'.format(reais, dólar))