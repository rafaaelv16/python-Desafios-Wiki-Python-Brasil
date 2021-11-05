from class_ponto import Ponto

from class_retangulo import Retangulo

def main():
    r = Retangulo(10,15)
    r2 = Retangulo(2,5)
    r3 = Retangulo(20, 50)

    n=0
    while n == 0:
        print("menu")
        print("1 - Alterar Valores do Retângulo")
        print("2 - Imprimir Centro do Retângulo")
        escolha = input()

        if escolha == '1':
            r.mudarValorRetangulo()
        elif escolha == '2':
            r.encontrarCentro()
        else:
            print("Escolha Inválida")

if __name__ == '__main__':  # chamada da funcao principal
    main()
