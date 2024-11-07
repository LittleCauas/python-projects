import library

sair = "N"


while sair.lower() == "n":
    library.exibir_titulo("# Calculador de média")
    n1 = float(input("Digite sua nota: "))
    n2 = float(input("Digite sua nota: "))
    media = (n1 + n2) / 2
    print(library.linha)
    print("A média é de: ", media)
    sair = library.sair()