"""
6 - Classe TV:

Faça um programa que simule um televisor criando-o como um objeto.

O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.

Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self,canal,volume):
        if (canal > 0) & (canal < 12):
            self.canal = canal
        else:
            print('Canal Inválido. Deve ser entre 1 - 11')
        if (volume > 0) & (volume <= 10):
            self.volume = volume
        else:
            print('Volume Inválido. Deve ser entre 1 - 10')

    def trocarCanal(self,canal):
        if (canal > 0) & (canal < 12):
            self.canal = canal
        else:
            print('Canal Inválido.')

    def aumentarVolume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print('Volume não pode exceder 10')

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Volume não pode ser menor que 0')

    def mostrarTV(self):
        print("A TV está no canal: ",self.canal)
        print("A TV está no volume: ",self.volume)


#testes abaixo
tv = TV(11,10)

tv.mostrarTV()

tv.trocarCanal(12)

tv.diminuirVolume()

tv.mostrarTV()