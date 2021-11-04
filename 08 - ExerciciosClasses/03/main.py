from class_retangulo import Retangulo

class main():
    ladoa = float(input('Digite o Lado A '))
    ladob = float(input('Digite o Lado B '))

    r = Retangulo(ladoa,ladob)
    print(f"Quantidade de Piso: {r.calcularArea()} m²")
    print(f"Quantidade de Rodapé: {r.calculaPerimetro()} m²")



if __name__ == "__main__":
    main()