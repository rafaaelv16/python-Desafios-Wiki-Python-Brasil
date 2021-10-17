#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

reais_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas_mes = float(input('Quantas horas você trabalha por mês? '))
salario_mes = reais_hora * horas_trabalhadas_mes

print(f'Seu salário no mês referido será de R$ {salario_mes:.2f}')