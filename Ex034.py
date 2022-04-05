# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# 
# Para salários superiores a R$1250,00 calcule um aumento de 10%.
# 
# Para salários inferiores ou iguais o aumento é de 15%.

salario = float(input('Digite o seu salário: R$'))



if salario <= 1250:
    menor = (salario * 0.15) + salario
    print('\nO seu salário receberá um aumento de 15%, sendo agora: R${:.2f}'.format(menor))
else:
    maior = (salario * 0.1) + salario
    print('O seu salário receberá um aumento de 10%, sendo agora: R${:.2f}'.format(maior))
print('PARABÉNS PELO AUMENTO')