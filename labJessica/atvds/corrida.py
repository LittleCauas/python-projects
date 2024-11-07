custoCorrida = 2.3
totalCorridas = 0
valorFinal = 0
while True:
    totalCorridas += 1

    placa = input("Informe a placa do carro: ")
    kmInicial = int( input("Informe a kilometragem inicial: "))
    kmFinal = int (input("Informe a kilometragem final: "))

    valorFinal += (kmFinal - kmInicial) * custoCorrida

    opco = input("Deseja continuar?S/N ")

    if opco.lower() == "n":
        break

print("O valor total foi de: " , valorFinal, " e o total de corridas foi de: " , totalCorridas)
