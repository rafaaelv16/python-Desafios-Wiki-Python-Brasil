"""
33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia
as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""

temperaturas = input('Digite as temperaturas separando-as por espaço ').split()
temperaturas_float = []

for i in temperaturas:
    temperaturas_float.append(float(i))

print(f"""Menor temperatura: {min(temperaturas_float)}
Maior temperatura: {max(temperaturas_float)}
Média das temperaturas: {sum(temperaturas_float)/len(temperaturas_float)}""")
