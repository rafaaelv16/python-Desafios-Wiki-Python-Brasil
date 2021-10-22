"""
41 - Faça um programa que receba o valor de uma dívida
e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
        1       0
        3       10
        6       15
        9       20
        12      25
    Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela

    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
"""

lista_parcela_juros = [[1,0],
                       [3,10],
                       [6,15],
                       [9,20],
                       [12,25]]

divida = 1000#float(input('Digite o valor da dívida: '))

print('Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela')
for i in lista_parcela_juros:
    valor_juros = divida_ajustada = 0

    numero_parcelas = i[0]
    valor_juros = divida * (i[1]/100)
    divida_ajustada = valor_juros + divida
    valor_parcelas = divida_ajustada / numero_parcelas
    print(f'{divida_ajustada}          | {valor_juros}           | {numero_parcelas}                       | {valor_parcelas:.2f}')


