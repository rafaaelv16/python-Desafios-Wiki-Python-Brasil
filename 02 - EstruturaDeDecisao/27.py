"""
27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

kg_morango = float(input('Quantos kg(s) de Morango?'))
kg_maca = float(input('Quantos kg(s) de Maçã?'))

preco_morango = 2.5
preco_maca = 1.8

if kg_morango > 5:
    preco_morango = 2.2

if kg_maca > 5:
    preco_maca = 1.5

total = (preco_morango * kg_morango) + (preco_maca * kg_maca)
kg_total = kg_morango + kg_maca

if (total > 25) | (kg_total > 8):
    total = total * 0.90

print(f'O valor total da compra é de {total}')