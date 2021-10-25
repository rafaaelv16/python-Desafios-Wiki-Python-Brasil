"""
48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
    Exemplo:
      12376489
      => 98467321

"""

n = int(input('Digite um valor inteiro'))

#invertendo o número
novo_n = int(str(n)[::-1])

print(f'{n} => {novo_n}')