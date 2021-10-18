"""
1 - Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
valor = int(input('Digite um valor entre zero e dez'))

while (valor < 0) | (valor > 10):
    valor = int(input('Valor Inválido.'
                      '\nDigite um valor entre zero e dez'))

print('Parabéns. Programa encerrado')

