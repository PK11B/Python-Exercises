# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "Silva" no nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Tem Silva? {}'.format('SILVA' in nome.upper()))

# procura = 'SILVA' in nome.upper()
# 
# if procura == True:
#   print('Tem Silva')
# else:
#   print('Não tem Silva')