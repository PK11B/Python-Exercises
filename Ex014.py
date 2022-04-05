# Faça uma calculadora que converta um valor em Celsius para Fahrenheit
c = float(input('Digite um valor em °C para ser convertido: '))
f = (c * 1.8) + 32
print('A temperatura de {}°C equivale a {:.1f}°F'.format(c, f))