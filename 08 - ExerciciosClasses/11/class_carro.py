"""
11 - Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    A - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    B - O consumo é especificado no construtor e o nível de combustível inicial é 0.
    C - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    D - Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    E - Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

"""
#consumo = 10KM/l

#autonomia = 10 * 10 => 100

#andar 90 km = 90 / consumo => 9   - sobrar 1 litro

class Carro:
    def __init__(self,consumo):
        self.consumo = consumo
        self.combustivelCarro = 0

    def andar(self,distancia):
        autonomia = self.consumo * self.combustivelCarro
        if autonomia > distancia:
            print(f'Carro andou {distancia} Kms')
            self.combustivelCarro -= distancia / self.consumo

        else:
            print(f'Carro não tem combustível suficiente!')

    def adicionarGasolina(self,litros):
        self.combustivelCarro += litros
        print(f'Você adicionou {litros} de gasolina')

    def obterGasolina(self):
        print(f'Combustível no tanque: {self.combustivelCarro:.2f} litros')

    def mostrarCarro(self):
        return self.consumo, self.combustivelCarro

meuFusca = Carro(15)

meuFusca.adicionarGasolina(20)

meuFusca.andar(100)

meuFusca.obterGasolina()