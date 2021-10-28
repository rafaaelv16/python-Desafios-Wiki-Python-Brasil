"""
23 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu
servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber
qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo,
chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres.
A partir deste arquivo, você deve criar um programa que gere um relatório,
chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB

Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória,
caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma
função separada, que será chamada pelo programa principal.

O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo
programa principal.

"""

f = open('usuarios.txt', 'r',encoding='utf-8')
usuario_espaco = []
megabytes = 0
conta_usuarios = 0
for line in f:
    n = line.split()
    usuario_espaco.append(n)

def bytes_megabytes(bytes):
    return round(bytes/1024/1024,2)

def calcular_percentual(utilizado_pelo_usuario):
    return (utilizado_pelo_usuario/megabytes)*100


for i in usuario_espaco:
    i[1] = bytes_megabytes(float(i[1]))
    megabytes += i[1]

for i in usuario_espaco:
    percentual = calcular_percentual(i[1])
    i.append(round(percentual, 2))

#limpando o arquivo
open('relatório.txt', 'w').close()

#criando o arquivo, que receberá append(adições)
with open('relatório.txt', 'a',encoding="utf-8") as arquivo:


    print("ACME Inc.               Uso do espaço em disco pelos usuários")
    print("ACME Inc.               Uso do espaço em disco pelos usuários", file=arquivo)


    print("-"*65)
    print("-"*65, file=arquivo)


    print("{:<5}{:<15}{:<25}{:<15}\n".format("Nr.","Usuário","Espaço utilizado","% do uso"))
    print("{:<5}{:<15}{:<25}{:<15}\n".format("Nr.","Usuário","Espaço utilizado","% do uso"), file=arquivo)

    numero_usuario = 0
    for i in usuario_espaco:
        numero_usuario+=1
        print("{:<5}{:<15}{:<25}{:<15}".format(numero_usuario,i[0],i[1],i[2]))
        print("{:<5}{:<15}{:<25}{:<15}".format(numero_usuario,i[0],i[1],i[2]), file=arquivo)

    print(f"\nEspaço total Ocupado: {megabytes} MB")
    print(f"\nEspaço total Ocupado: {megabytes} MB", file=arquivo)
    print(f"\nEspaço médio ocupado: {megabytes/len(usuario_espaco):.2f} MB")
    print(f"\nEspaço médio ocupado: {megabytes/len(usuario_espaco):.2f} MB", file=arquivo)