"""
26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro


Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""

print('### Posto de Gasolina ###')
litros = int(input('Quantos litros?'))
tipo_combustivel = input('Qual o tipo de combustível? A-álcool, G-gasolina')

preco_alcool = 1.90
preco_gasolina = 2.50

total = 0

if tipo_combustivel == 'A':
    combustivel = 'Álcool'
    if litros <= 20:
        desconto = 3
        total = (preco_alcool * 0.97) * litros
    else:
        desconto = 5
        total = (preco_alcool * 0.95) * litros

if tipo_combustivel == 'G':
    combustivel = 'Gasolina'
    if litros <= 20:
        desconto = 4
        total = (preco_gasolina * 0.96) * litros
    else:
        desconto = 6
        total = (preco_gasolina * 0.94) * litros

print(f"""Você optou por comprar {combustivel}, como você comprou {litros} litros,
teve um desconto de {desconto}% por litro.
O total deu: {total}""")