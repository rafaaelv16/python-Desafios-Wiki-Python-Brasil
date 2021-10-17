#3 - Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# A) Para homens: (72.7*h) - 58
# B) Para mulheres: (62.1*h) - 44.7


altura = float(input('Digite a sua altura '))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(f'Homem, Seu peso ideal é {peso_ideal_homem:.2f}')
print(f'Mulher, Seu peso ideal é {peso_ideal_mulher:.2f}')