"""
47 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7

    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04
"""
melhor_salto = pior_salto = 0
notas = []

nome = input('Nome do participante.\n')

for i in range(1,8):
    nota = -1
    while (nota < 0) | (nota > 10):
        nota = float(input(f'Nota: '))
        if (nota < 0) | (nota > 10):
            print('Nota Inválida. Tente novamente!')
    notas.append(nota)

print(f"""\nAtleta: {nome}""")

for i in notas:
    print(f'Nota: {i}')

#definindo a melhor e pior nota
melhor_salto = max(notas)
pior_salto = min(notas)

#removendo melhor e pior saltos
notas.remove(melhor_salto)
notas.remove(pior_salto)

print(f"""\nResultado Final:
Atleta: {nome} 
Melhor Nota: {melhor_salto}
Pior Nota: {pior_salto}
Média: {(sum(notas))/len(notas):.2f}""")