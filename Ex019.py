# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quatro aluno: ')
lista = [n1, n2, n3, n4]
escolha = choice(lista)
print('O aluno escolhido foi {}!'.format(escolha))