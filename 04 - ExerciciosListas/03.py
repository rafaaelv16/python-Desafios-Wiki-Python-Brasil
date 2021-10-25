"""
3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []

for i in range(1,5):
    nota = -1
    while (nota < 0) | (nota > 10):
        nota = float(input(f'Digite a nota do {i}º bimestre: '))
        if (nota < 0) | (nota > 10):
            print('Nota Inválida, tente novamente!')
    notas.append(nota)

print('Notas')
print('{:<15} {:<8}'.format("Bimestre","Nota"))

bim = 1

for i in notas:
    print('{:<15} {:<8}'.format(bim,i))
    bim += 1

print(f'\nMédia é: {sum(notas)/len(notas)}')