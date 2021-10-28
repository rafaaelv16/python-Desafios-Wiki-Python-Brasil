"""
19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final
o resultado da mesma.

O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada
um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

#função para calcular o percentual
def calcular_percentual(total_votos,votos_no_candidato):
    percentual = (votos_no_candidato / total_votos) * 100
    return percentual



print("""Qual o melhor Sistema Operacional para uso em servidores?

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro""")

n = -1
total_votos = mais_voto = 0
sistemas = []
melhor = []

sistemas = [["Windows Server"],
          ["Unix"],
          ["Linux"],
          ["Netware"],
          ["Mac OS"],
          ["Outro"]]

#popualando a lista votos com número 1 ao 23, com o 0 ao lado que siginifica a quantidade de votos e o percentual = 0
for i in sistemas:
    i.append(0)
    i.append(0)

print(sistemas)

while (n != 0) | (n > 6):
    n = int(input('Melhor Sistema (0=fim):'))

    if (n > 6) | (n < 0):
        print('Informe um valor entre 1 e 6 ou 0 para sair!')

    #se o voto for válido, entra pra contagem
    elif n != 0:
        total_votos += 1
        sistemas[n-1][1] += 1

#percorrendo a lista de votos
for i in sistemas:
    # atribuindo o valor do percentual ao 3 elemento de cada sublista que representa o jogador
    if i[1] > 0:
        i[2] = calcular_percentual(total_votos,i[1])

#imprimindo a quantidade de votos computados
print(f"""Resultado da votação:\n\nForam computados {total_votos} votos.\n""")


#criando o cabeçalho da tabulação "Jogador","Votos","%"
print("{:<20} {:<10} {:<10}".format("Sistema Operacional","Votos","%"))
print("-"*20,"-"*10,'-'*10)

#percorrendo a lista de votos pra mostrar a quantidade de votos e percentual de votos de cada jogador que teve mais de 0 votos
for i in sistemas:
    #imprimindo jogador
    print("{:<20} {:<10} {:<10.1f}%".format(i[0],i[1],i[2]))

    #pegando o jogador com mais votos e adicionando ele em uma lista única pra mostrar posteriormente
    if i[1] > mais_voto:
        mais_voto = i[1]
        melhor.clear()
        melhor.append(i)




print("-"*20,"-"*10,'-'*10)

print("Total"," "*14,f"{total_votos}")

#imprimindo qual foi o jogador que recebeu mais votos
print(f"""O melhor jogador foi o número {melhor[0][0]}, com {melhor[0][1]} votos, correspondendo a {melhor[0][2]:.1f}% do total de votos.""")

