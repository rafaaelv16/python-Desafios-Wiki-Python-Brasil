"""
25 - Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

lista_idade = input('Digite as idades separando-as por espaço ').split()

soma = media = 0

for i in lista_idade:
    soma += int(i)

media = soma/len(lista_idade)

print(f'A média de idade é: {media}')

if media <= 25:
    print('Jovem')
elif media <= 60:
    print('Adulta')
else:
    print('Idosa')

