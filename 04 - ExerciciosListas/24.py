"""
24 - Faça um programa que simule um lançamento de dados.

Lance o dado 100 vezes e armazene os resultados em um vetor .

Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
simulando os lançamentos dos dados.
"""
import random
numeros_caidos = []
for i in range(0,100):
    numeros_caidos.append(random.randint(1,6))

for i in range(1,7):
    print(f"O valor {i} foi obtido {numeros_caidos.count(i)} vezes")


