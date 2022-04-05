# Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
maior = primeiro
menor = primeiro

# Maiores

if segundo > primeiro and segundo > terceiro:
    maior = segundo

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

# Menores

if segundo < primeiro and segundo < terceiro:
    menor = segundo

if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print('\nO maior valor digitad foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))