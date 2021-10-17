"""
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o
    reajuste segundo o seguinte critério, baseado no salário atual:

        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5%

        Após o aumento ser realizado, informe na tela:
            o salário antes do reajuste;
            o percentual de aumento aplicado;
            o valor do aumento;
            o novo salário, após o aumento.

"""

salario = float(input('Digite o seu salário: '))

percentual_de_aumento = 0

if salario <= 280:
    percentual_de_aumento = 20

elif salario < 700:
    percentual_de_aumento = 15

elif salario < 1500:
    percentual_de_aumento = 10

else:
    percentual_de_aumento = 5


print(f"""O salário antes do reajuste era de R$ {salario:.2f}
o percentual de aumento foi de {percentual_de_aumento}%
o valor do aumento foi de R$ {(percentual_de_aumento/100)*salario:.2f}
o novo salário é de R$ {((percentual_de_aumento/100)*salario)+salario:.2f}""")