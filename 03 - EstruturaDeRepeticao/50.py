"""
50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.

"""
#n = int(input('Digite quantos termos serão calculados'))
n = 5
resultado = 'H = '
anterior = soma = 0

for i in range(1,n+1):
    if (i < n):
        resultado += f"1/{(1 + anterior)} + "
    else:
        resultado += f"1/{(1 + anterior)}"

    soma = 1/(i+anterior)

    anterior = i

print(f'{resultado} = {soma}')