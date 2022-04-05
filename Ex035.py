# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não 
# formar um triângulo.

print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
primeiro = float(input('\nDigite o valor do primeiro lado: '))
segundo = float(input('Digite o valor do segundo lado: '))
terceiro = float(input('Digite o valor do terceiro lado: '))
condição_existencia = bool(abs(segundo - terceiro) < primeiro and  primeiro < (segundo + terceiro))

if condição_existencia == True:
    print('Este triângulo existe')
else:
    print('Este triângulo não existe')