from class_ponto import Ponto
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def mudarValorRetangulo(self):
        self.largura = float(input('Digite nova largura '))
        self.altura = float(input('Digite nova altura '))

    def retornarValorRetangulo(self):
        self.largura
        self.altura

    def calcularArea(self):
        return self.largura * self.altura

    def calculaPerimetro(self):
        return (self.largura + self.altura) * 2

    def encontrarCentro(self):
        largura = self.largura / 2
        altura = self.altura / 2
        p = Ponto(largura,altura)
        p.imprimirPontos()

