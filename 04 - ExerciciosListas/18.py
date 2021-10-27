"""
18 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores
para saber qual o melhor jogador após cada jogo.

Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa,
utilizando a linguagem de programação C++.

Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo,
mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

O total de votos computados;

Os números e respectivos votos de todos os jogadores que receberam votos;

O percentual de votos de cada um destes jogadores;

O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos
e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos.
O resultado aparece ordenado pelo número do jogador.
O programa deve fazer uso de arrays.
O programa deverá executar o cálculo do percentual de cada jogador através de uma função.
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado.
Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa.
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo
texto no disco, obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador         Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""

#limpando o arquivo
open('Resultado Eleições.txt', 'w').close()

#criando o arquivo, que receberá append(adições)
with open('Resultado Eleições.txt', 'a',encoding="utf-8") as arquivo:

    #função para calcular o percentual
    def calcular_percentual(total_votos,votos_no_candidato):
        percentual = (votos_no_candidato / total_votos) * 100
        return percentual


    n = -1
    total_votos = maior_voto = 0
    votos = []
    ranking_melhores = []
    #popualando a lista votos com número 1 ao 23, com o 0 ao lado que siginifica a quantidade de votos e o percentual = 0
    for i in range(1,24):
        votos.append([i,0,0])

    #condição para que o voto seja válido: 1 - 23, se for 0 saia do programa
    while (n != 0) | (n > 23):

        #captura do voto
        n = int(input('Número do jogador (0=fim):'))

        #gravando captura do voto no arquivo
        print(f'Número do jogador (0=fim): {n}', file=arquivo)

        #Se o voto for inválido, isso será informado ao usuário
        if (n > 23) | (n < 0):
            print('Informe um valor entre 1 e 23 ou 0 para sair!')

            # gravando voto inválido no arquivo
            print('Informe um valor entre 1 e 23 ou 0 para sair!', file=arquivo)

        #se o voto for válido, entra pra contagem
        elif n != 0:
            total_votos += 1
            votos[n-1][1] += 1

    #percorrendo a lista de votos
    for i in votos:
        #se o jogador recebeu mais de um voto será impresso no resultado, será calculado o percentual
        if i[1] > 0:
            #atribuindo o valor do percentual ao 3 elemento de cada sublista que representa o jogador
            i[2] = calcular_percentual(total_votos,i[1])

    #imprimindo a quantidade de votos computados
    print(f"""Resultado da votação:\n\nForam computados {total_votos} votos.\n""")

    #gravando a quantidade de votos computados no arquivo
    print(f"""Resultado da votação:\n\nForam computados {total_votos} votos.\n""", file=arquivo)

    #criando o cabeçalho da tabulação "Jogador","Votos","%"
    print("{:<10} {:<10} {:<10}".format("Jogador","Votos","%"))

    #gravando o cabeçalho da tabulação "Jogador","Votos","%" no arquivo
    print("{:<10} {:<10} {:<10}".format("Jogador","Votos","%"),file=arquivo)

    #percorrendo a lista de votos pra mostrar a quantidade de votos e percentual de votos de cada jogador que teve mais de 0 votos
    for i in votos:
        if i[1] > 0:
            #imprimindo jogador
            print("{:<10} {:<10} {:<10.1f}".format(i[0],i[1],i[2]))

            #gravando votos no jogador no arquivo
            print("{:<10} {:<10} {:<10.1f}".format(i[0],i[1],i[2]),file=arquivo)

            #pegando o jogador com mais votos e adicionando ele em uma lista única pra mostrar posteriormente
            if i[1] > maior_voto:
                maior_voto = i[1]
                ranking_melhores.clear()
                ranking_melhores.append(i)


    #imprimindo qual foi o jogador que recebeu mais votos
    print(f"""O melhor jogador foi o número {ranking_melhores[0][0]}, com {ranking_melhores[0][1]} votos, correspondendo a {ranking_melhores[0][2]:.1f}% do total de votos.""")

    #gravando qual foi o jogador que recebeu mais votos no arquivo
    print(f"""O melhor jogador foi o número {ranking_melhores[0][0]}, com {ranking_melhores[0][1]} votos, correspondendo a {ranking_melhores[0][2]:.1f}% do total de votos.""",file=arquivo)