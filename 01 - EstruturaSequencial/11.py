# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#    A) o produto do dobro do primeiro com metade do segundo .
#    B) a soma do triplo do primeiro com o terceiro.
#    C) o terceiro elevado ao cubo.

inteiro1 = int(input('Digite o primeiro valor inteiro '))
inteiro2 = int(input('Digite o primeiro valor inteiro '))

real = float(input('Digite o valor Real '))

a = (inteiro1 * 2) + (inteiro2 / 2)
b = (inteiro1 * 3) + real
c = real ** 3

print(f'o produto do dobro do primeiro com metade do segundo é {a}')
print(f'a soma do triplo do primeiro com o terceiro é {b}')
print(f'o terceiro elevado ao cubo é {c}')