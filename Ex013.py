# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salário = float(input('Digite o valor do seu salário: R$ '))
aumento = salário + (salário*(15/100))
print('O seu salário passa a ser {:.2f} com o aumento'.format(aumento))