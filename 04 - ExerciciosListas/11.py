"""
11 - Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.

11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor_a = [1,5,6,9,9,7,15,19,87,100]
vetor_b = [2,6,9,78,74,52,61,20,32,312]
vetor_c = [1,2,3,4,5,6,7,8,9,3]
vetor_d = [*sum(zip(vetor_a,vetor_b,vetor_c),())]

print(vetor_d)