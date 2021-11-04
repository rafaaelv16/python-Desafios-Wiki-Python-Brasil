"""
1 - Classe Bola: Crie uma classe que modele uma bola:

    A - Atributos: Cor, circunferência, material
    B - Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self,cor, circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor


#testes abaixo

#instanciando a classe bola
b = Bola('azul',15,'plastico')

#imprimir cor
print(b.mostraCor())

#trocar a cor
b.trocaCor('vermelha')

#imprimir cor
print(b.mostraCor())
