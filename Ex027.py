# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = str(input('Digite o seu nome completo: ')).strip()
split = nome.split()
print('O seu primeiro nome é {}'.format(split[0]))
print('O seu último nome é {}'.format(split[-1]))