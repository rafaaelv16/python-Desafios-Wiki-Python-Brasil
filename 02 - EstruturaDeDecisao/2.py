#2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input('Digite o primeiro número '))
pos_neg = 'positivo'

if n1 < 0:
    pos_neg = 'negativo'

print(f'O número digitado é {pos_neg}')
