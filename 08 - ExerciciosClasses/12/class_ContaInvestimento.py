"""
12 - Classe Conta de Investimento:

Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo
taxaJuros.

Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.

Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.

Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

"""

class ContaInvestimento:
    def __init__(self,saldo=1000,taxa_juros=10):
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def adicionarJuros(self):
        self.saldo += self.saldo*(self.taxa_juros/100)

    def mostrarConta(self):
        print(f'Saldo: R$ {self.saldo}\nTaxa de Juros: {self.taxa_juros}')


CC = ContaInvestimento()

CC.adicionarJuros()

CC.mostrarConta()