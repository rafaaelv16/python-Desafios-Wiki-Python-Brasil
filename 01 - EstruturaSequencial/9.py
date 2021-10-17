#9 - Faça um Programa que peça a temperatura em graus Fahrenheit
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input('Digite a temperatura em Graus Fahrenheit '))
celsius = 5*((fahrenheit - 32) / 9 )

print(f'A temperatura de {fahrenheit} graus Fahrenheit equivale a {celsius:.2f} graus Celsius')