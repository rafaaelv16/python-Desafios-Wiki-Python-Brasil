"""
49 - Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""
n = int(input('Digite quantos termos serão calculados'))
resultado = 'S = '
anterior = soma = 0
for i in range(1,n+1):
    if (i < n):
        resultado += f"{i}/{(i + anterior)} + "
    else:
        resultado += f"{i}/{(i + anterior)}"

    soma = i/(i+anterior)

    anterior = i

print(f'{resultado} = {soma}')