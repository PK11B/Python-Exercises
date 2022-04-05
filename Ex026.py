# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição aparece a primeira vez
# 3 - Em que posição aparece a última vez

frase = str(input('Escreva uma frase: ')).lower().strip()
print("A letra 'A' aparece {} vezes nessa frase".format(frase.count('a')))
print("A letra 'A' aparece pela primeira vez na {}ª posição".format(frase.find('a') + 1))
print("A letra 'A' aparece pela última vez na {}ª posição".format(frase.rfind('a') + 1))