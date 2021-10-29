"""
14 - Quadrado mágico.
Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e
no qual a soma das linhas, colunas e diagonais é a mesma.

Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características
acima.

Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.

Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""
import random

vetor = [1,2,3,4,5,6,7,8,9]
sequencias_exclusivas = []

#descobrindo o número de sequencias diferentes que a lista pode ter
qtd_sequencias_diferentes = 1
for i in range(1,len(vetor)+1):
    qtd_sequencias_diferentes *= i

conta = 1
j = 10000
while len(sequencias_exclusivas) != qtd_sequencias_diferentes:
    random.shuffle(vetor)

    if vetor not in sequencias_exclusivas:
        #print('Adicionando ao vetor exclusivo')
        sequencias_exclusivas.append([vetor[0],vetor[1],vetor[2],
                                      vetor[3],vetor[4],vetor[5],
                                      vetor[6],vetor[7],vetor[8]])

    if len(sequencias_exclusivas) >= j:
        print(conta,len(sequencias_exclusivas),qtd_sequencias_diferentes)
        j += 20000

    conta+=1
print(conta,len(sequencias_exclusivas),qtd_sequencias_diferentes)

def identificaMostraQuadradosMagicos(lista):

    for i in lista:
        if (i[0]+i[1]+i[2] == i[3]+i[4]+i[5]) & (i[0]+i[1]+i[2] == i[2]+i[4]+i[6]):
            for j in range(0, len(i), 3):
                print(matriz[j], matriz[j + 1], matriz[j + 2])

identificaMostraQuadradosMagicos(sequencias_exclusivas)

"""
vetor = [1,2,3]
novo = []
vetor2=[5,9,3]


if vetor not in novo:
    novo.append(vetor)
    print('Não Está no vetor')

if vetor2 not in novo:
    novo.append(vetor2)
    print('Não Está no vetor')

if vetor2 not in novo:
    novo.append(vetor2)
    print('Não Está no vetor')
else:
    print('Já se encontra no vetor')

print(novo)"""