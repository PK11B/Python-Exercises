# Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um valor: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2) # se quisesse poderia ter importado a biblioteca 'math' e ter feito 'math.sqrt(n1)'
print('Valor escolhido: {}\nSeu dobro: {}\nTriplo: {}\nSua raiz: {:.2f}'.format(n1, dobro, triplo, raiz))