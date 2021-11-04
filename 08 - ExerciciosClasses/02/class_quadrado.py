"""
2 - Classe Quadrado: Crie uma classe que modele um quadrado:

    A - Atributos: Tamanho do lado
    B - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""

class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudarValorLado(self,lado):
        self.lado = lado

    def retornaLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado * 4


#testes abaixo
q = Quadrado(10)

print(q.retornaLado())

q.mudarValorLado(5)

print(q.calcularArea())