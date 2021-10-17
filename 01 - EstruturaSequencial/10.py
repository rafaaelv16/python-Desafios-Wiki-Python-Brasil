# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# C = 5 * ((F-32) / 9).


celsius = float(input('Digite a temperatura em Graus Celsius '))
fahrenheit = (celsius * 1.8) + 32

print(f'A temperatura de {celsius:.2f} graus Celsius equivale a {fahrenheit:.2f} graus Fahrenheit')