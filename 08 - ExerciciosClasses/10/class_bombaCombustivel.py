"""
10 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    A - Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        i - tipoCombustivel.
        ii - valorLitro
        iii - quantidadeCombustivel

    B - Possua no mínimo esses métodos:
        i - abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        ii - abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        iii - alterarValor( ) – altera o valor do litro do combustível.
        iv - alterarCombustivel( ) – altera o tipo do combustível.
        v - alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

"""

class BombaCombustivel():
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valor):
        litros = valor / self.valorLitro
        if self.quantidadeCombustivel > litros:
            print(f'Serão abastecidos {litros} Litros')
            self.quantidadeCombustivel -= litros
        else:
            print('Nosso combustível acabou infelizmente')

    def abastecerPorLitro(self,litros):
        valor = litros * self.valorLitro
        if self.quantidadeCombustivel > litros:
            print(f'Valor a ser pago: R$ {valor}')
            self.quantidadeCombustivel -= litros
        else:
            print('Nosso combustível acabou infelizmente')

    def alterarValor(self,valor):
        self.valorLitro = valor

    def alterarQuantidadeCombustivel(self,quantidade):
        self.quantidadeCombustivel = quantidade

    def mostraBomba(self):
        print(f"""Tipo de Combustível: {self.tipoCombustivel}
Valor do Litro: R$ {self.valorLitro}
Quantidade na Bomba: {self.quantidadeCombustivel} litros""")


gasolina = BombaCombustivel('Gasolina',6.89, 1000)

gasolina.mostraBomba()

gasolina.abastecerPorValor(689)

gasolina.mostraBomba()

gasolina.abastecerPorLitro(800)

gasolina.mostraBomba()

gasolina.alterarValor(1)

gasolina.mostraBomba()

gasolina.abastecerPorLitro(800)

gasolina.mostraBomba()