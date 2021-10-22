"""
40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes
de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).

    Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

"""

#conjunto = input('Digite cinco conjuntos com 3 valores: código cidade, número de veículos e número de acidentes de trânsito com vítimas').split()
conjunto = [1,1500,69,
            2,2500,47,
            3,3000,190,
            4,1000,50,
            5,10000,500]

lista = []
menor_indice_acidente = 1000
maior_indice_acidente = qtde_veiculos = cidades_ate_dois_mil_veiculos = soma_cidades_ate_dois_mil_veiculos = 0

for i in range(0,15,3):
    lista.append([conjunto[i],conjunto[i+1],conjunto[i+2]])

for i in lista:
    código_cidade = i[0]
    numero_veiculos = int(i[1])
    acidentes_com_vitimas = int(i[2])

    indice_acidentes = 100 / (numero_veiculos / acidentes_com_vitimas)

    qtde_veiculos += numero_veiculos

    # descobrindo o mais alto
    if indice_acidentes > maior_indice_acidente:
        maior_indice_acidente = indice_acidentes
        cod_maior_indice_acidente = i[0]

    # descobrindo o mais baixo
    if indice_acidentes < menor_indice_acidente:
        menor_indice_acidente = indice_acidentes
        cod_menor_indice_acidente = i[0]

    if numero_veiculos < 2000:
        cidades_ate_dois_mil_veiculos += 1
        soma_cidades_ate_dois_mil_veiculos += acidentes_com_vitimas

media = qtde_veiculos / len(lista)
media_acidentes_ate_dois_mil_veiculos = soma_cidades_ate_dois_mil_veiculos / cidades_ate_dois_mil_veiculos

print(f"""O maior índice de acidentes de trânsito é {maior_indice_acidente:.2f}% da cidade {cod_maior_indice_acidente}
O menor índice de acidentes de trânsito é {menor_indice_acidente:.2f}% da cidade {cod_menor_indice_acidente}
A média é de {media} veículos por cidade
A média de acidentes de trânsito nas cidades com menos de 2.000 veículos é de {media_acidentes_ate_dois_mil_veiculos}""")

