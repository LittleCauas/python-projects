import lib
import os

sair = "n"

while sair.lower == "n":
    os.system("cls")
    print("# MENU #")
    print("Digite o número correspondente a opção desejada")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Sair")
    print()
    opc = int(input("R: "))
    os.system("cls")

    if opc == 1:
        lib.adicionar(input("Nome: "))
    elif opc == 2:
        lib.listar()
        os.system("pause")
    else:
        sair = input("Deseja sair? S/N ")
        if sair.lower() == "s":
            sair.lower() == "s"
        else:
            continue

