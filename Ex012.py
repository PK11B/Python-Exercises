# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Digite o valor do produto: R$ '))
desconto = produto - (produto*(5/100))
print('O preço ficará R${:.2f} com o desconto de 5%'.format(desconto))