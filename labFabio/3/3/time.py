import lib
import os

opcao = 0
sair = "n"
while sair == "n":
    os.system("cls")
    print("### MENU ###")
    print("1. Adicionar jogador")
    print("2. Listar jogadores")
    print("3. Pesquisar jogador")
    print("4. Sair")
    opc = int(input("R. "))
    os.system("cls")

    if opc == 1:
        lib.adicionar(input("Nome: "))

    elif opc == 2:
        lib.visualizar()

    elif opc == 3:
        lib.pesquisar(int(input("Número da camisa: ")))

    else:
        sair = "s"

    os.system("pause")