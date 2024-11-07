totalidade = 0
while True:
    totalpre += int(input("Informe o preço: "))

    opco = input("Deseja continuar?S/N ")

    if opco.lower() == "n":
        break

print("A idade total é de: " , totalidade)
