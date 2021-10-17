"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    A) salário bruto.
    B) quanto pagou ao INSS.
    C) quanto pagou ao sindicato.
    D) o salário líquido.
    E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""


reais_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas_mes = float(input('Quantas horas você trabalha por mês? '))
salario_bruto = reais_hora * horas_trabalhadas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos



print(f'A) salário bruto: R$ {salario_bruto:.2f}')
print(f'B) quanto pagou ao INSS: R$ {inss:.2f}')
print(f'C) quanto pagou ao sindicato: R$ {sindicato:.2f}')
print(f'D) o salário líquido: R$ {salario_liquido:.2f}')
print(f"""E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$ {salario_bruto}
        - IR (11%) : R$ {ir}
        - INSS (8%) : R$ {inss}
        - Sindicato ( 5%) : R$ {sindicato}
        = Salário Liquido : R$ {salario_liquido}""")
