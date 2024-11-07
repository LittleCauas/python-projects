precototal = 0

while True:

    input("Informe o nome do produto: ")

    precototal += int(input("Informe o preço do produto: "))

    opco = input("Deseja continuar?S/N ")

    if opco.lower() == "n":
        break

print("A soma total dos produtos é de: " , precototal)
