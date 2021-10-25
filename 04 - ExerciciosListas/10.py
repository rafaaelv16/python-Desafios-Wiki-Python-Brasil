"""
10 - Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.
"""

vetor_a = [1,5,6,9,9,7,15,19,87,100]
vetor_b = [2,6,9,78,74,52,61,20,32,312]

vetor_c = [*sum(zip(vetor_a,vetor_b),())]

print(vetor_c)
