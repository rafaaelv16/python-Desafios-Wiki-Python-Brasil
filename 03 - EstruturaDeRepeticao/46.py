"""
46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos.

No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.

Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
em seus saltos e depois informe a média dos saltos conforme
a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m
"""
nome = 'participante'
melhor_salto = pior_salto = 0
notas = []

while nome != '':
    nome = input('Nome do participante. Caso queira terminar o programa, deixe vazio\n')
    if nome != '':
        for i in range(1,6):
            nota = -1
            while (nota < 0) | (nota > 10):
                nota = float(input(f'Nota {i}º salto: '))
                if (nota < 0) | (nota > 10):
                    print('Nota Inválida. Tente novamente!')
            notas.append(nota)

        print(f"""\nAtleta: {nome}""")
        cont = 0
        for i in notas:
            cont += 1
            print(f'{cont}º salto: {i} m')

        melhor_salto = max(notas)
        pior_salto = min(notas)

        print(f'\nMelhor salto: {melhor_salto} m')
        print(f'Pior salto: {pior_salto} m')

        #removendo melhor e pior saltos
        notas.remove(melhor_salto)
        notas.remove(pior_salto)

        print(f"""Média dos Saltos: {(sum(notas))/len(notas):.1f} m""")
        print(f"""\nResultado Final:
{nome}: {(sum(notas))/len(notas):.1f} m""")