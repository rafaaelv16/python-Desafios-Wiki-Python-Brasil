"""
13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número.

Não utilize a função de potência da linguagem.

"""
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
total = 1
for i in range(1,expoente+1):
    total *= base

print(f'{base} elevado a {expoente} = {total}')