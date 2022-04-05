# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km foram rodados? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preço = (0.15 * km) + (60 * dias)
print('De acordo com as informações prestadas acima o preço final a se pagar é de R${:.2f}'.format(preço))