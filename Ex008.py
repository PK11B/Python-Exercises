# Faça um programa que leia valor em metros e converta ele em centímetros e milímetros
m = float(input('Digite um valor em metros: '))
cm = int(m * 100)
mm = int(m * 1000)
print('{} metros equivalem\n{} centímetros\n{} milímetros'.format(m, cm, mm))