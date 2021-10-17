""" 17 - Faça um Programa para uma loja de tintas.
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
    em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    A) comprar apenas latas de 18 litros;
    B) comprar apenas galões de 3,6 litros;
    C) misturar latas e galões, de forma que o desperdício de tinta seja menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

area = int(input('Qual o tamanho da área a ser pintada?'))

#lata
preco_lata = 80
area_por_lata = 6 * 18
qtde_de_latas = area / area_por_lata
qtde_de_latas = math.ceil(qtde_de_latas)

#falão
preco_gl = 25
area_por_gl = 6 * 3.6
qtde_de_gl = area / area_por_gl
qtde_de_gl = math.ceil(qtde_de_gl)

print(f"""A) comprar apenas latas de 18 litros
      Serão usadas {qtde_de_latas:.0f} lata(s) de tinta a um custo total de R$ {qtde_de_latas * preco_lata}""")

print(f"""B) comprar apenas galões de 3,6 litros;
      Serão usadas {qtde_de_gl:.0f} Galão(ões) de tinta a um custo total de R$ {qtde_de_gl * preco_gl}""")

#lata+galão

area = area * 1.10

gl_qtde = 0
lata_qtde = 0

if area < (area_por_gl*4):
    gl_qtde = area / area_por_gl
    gl_qtde = math.ceil(gl_qtde)

    print(f"""C) misturar latas e galões, de forma que o desperdício de tinta seja menor
          Serão usadas {gl_qtde:.0f} galões de tinta 
          A um custo total de R$ {(gl_qtde * preco_gl)}""")

elif area <= area_por_lata:
    lata_qtde =+ 1

    print(f"""C) misturar latas e galões, de forma que o desperdício de tinta seja menor
          Serão usadas {lata_qtde:.0f} latas de tinta
          A um custo total de R$ {(lata_qtde * preco_lata)}""")
else:
    lata_qtde = area / area_por_lata
    lata_qtde = math.floor(lata_qtde)
    area_restante = area - (area_por_lata*lata_qtde)
    gl_qtde = area_restante / area_por_gl
    gl_qtde = math.ceil(gl_qtde)

    print(f"""C) misturar latas e galões, de forma que o desperdício de tinta seja menor
          Serão usadas {gl_qtde:.0f} galões de tinta 
          E
          Serão usadas {lata_qtde:.0f} latas de tinta
          A um custo total de R$ {(gl_qtde * preco_gl) + (lata_qtde * preco_lata)}""")
