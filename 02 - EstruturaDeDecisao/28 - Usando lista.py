"""28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra:

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento,
    valor do desconto
    valor a pagar.
"""

tipo_carne = tipo_pagamento = ''

while tipo_carne not in ('F','A','P'):
    tipo_carne = input("""Escolha o tipo de carne:
        F - Filé Duplo
        A - Alcatra
        P - Picanha
    """).upper()

kilos = float(input('Digite a quantidade, em kilos'))

pagamento = 'D'

nome_pagamento = 'Dinheiro'

preco_kilo = preco_total = descontos = 0

lista_carnes = [('F', 'Filé Duplo', 4.9, 5.8), ('Alcatra', 'Alcatra', 5.9, 6.8),('P', 'Picanha', 6.9, 7.8)]

op = 0
if tipo_carne == 'A': op = 1
elif tipo_carne == 'P': op = 2

preco_kilo = lista_carnes[op][2]

if kilos > 5:
    preco_kilo = lista_carnes[op][3]


while tipo_pagamento not in ('D','C'):
    tipo_pagamento = input('Digite o tipo de pagamento: D - Dinheiro; C - Cartão Tabajara').upper()

preco_total = preco_kilo * kilos

if tipo_pagamento == 'C':
    nome_pagamento = 'Cartão Tabajara'
    descontos = (preco_kilo * kilos) * 0.05

print(f"""Tipo de carne: {lista_carnes[op][1]}
Quantidade: {kilos} Kg
Preço Total: R$ {preco_total:.2f}
Tipo de Pagamento: {nome_pagamento}
Valor Desconto: {descontos:.2f}
Valor a Pagar: R$ {preco_total - descontos:.2f}""")