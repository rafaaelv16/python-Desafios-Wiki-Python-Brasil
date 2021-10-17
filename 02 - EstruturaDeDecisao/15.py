"""
15 - Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""
print('###Verifique se podemos formar um triângulo###')

n1 = float(input('Digite o primeiro lado '))
n2 = float(input('Digite o segundo lado '))
n3 = float(input('Digite o terceiro lado '))

if ((n2 + n3) > n1) & ((n1 + n3) > n2) & ((n1 + n2) > n3):
    print('Podemos formar um triângulo!')

    if n1 == n2 == n3:
        print('Este é um Triângulo Equilátero: três lados iguais.')

    elif (n1 == n2) | (n1 == n3) | (n2 == n3):
        print('Este é um Triângulo Isósceles: quaisquer dois lados iguais.')

    else:
        print('Este é um Triângulo Escaleno: três lados diferentes.')
else:
    print('Os lados apresentados não são capazes de formar um triângulo!')

