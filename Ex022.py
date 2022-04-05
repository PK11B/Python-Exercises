# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas as letras minúsculas
# 3 - Quantas letras ao todo (sem considerar os espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()
espaço = nome.replace(' ', '')
dividir = nome.split()
print('O seu nome em maiúsculas: {}'.format(nome.upper()))
print('O seu nome em minúsculas: {}'.format(nome.lower()))
print('O seu nome possui: {} letras'.format(len(espaço)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividir[0], len(dividir[0])))

# Linha 12 também pode ser: 
# 
# print('O seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
# 
# Dessa forma o número de espaços seria subtraído do número total de letras