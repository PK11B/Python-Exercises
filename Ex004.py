# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo: ') # Se o tipo primitivo não for definido ele será uma string
print('{} é do tipo: {}'.format(n, type(n)))
print('{} é numérico?'.format(n), n.isnumeric())
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é alfanumérico?'.format(n), n.isalnum())
print('{} está em maiúsculas?'.format(n), n.isupper())
print('{} está em minúsculas?'.format(n), n.islower())