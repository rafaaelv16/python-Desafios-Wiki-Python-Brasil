"""
programa anterior
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
    Ex.: 5!=5.4.3.2.1=120

20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""
continuar = True


while (continuar == True):
    numero = -1
    while (numero < 0) | (numero > 16):
        numero = int(input('Digite um número e descubra o fatorial do mesmo, de 0 a 16: '))
        if (numero < 0) | (numero > 16):
            print('Você digitou um valor fora do range 0 a 16 ')
    fatorial = 1

    for i in range(1,numero+1):
        fatorial *= i

    print(f'O fatorial de {numero} é igual a {fatorial}')