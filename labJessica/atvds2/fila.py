import library
import os

sair = "N"
opc = 0

while sair.lower() == "n":
    os.system("cls")
    print("## MENU ##")
    print("1. Atendimento")
    print("2. Visualizar Atendimento")
    print("3. Chamar próxima senha")
    print("4. Quantidade de atendimentos disponiveis")
    print("5. Sair")
    opc = int(input("R. "))
    os.system("cls")
    if opc == 1:
        library.adicionar(input("Nome: "))
    elif opc == 2:
        library.visualizar()
    elif opc == 3:
        library.prox_senha()
    elif opc == 4:
        library.disponiveis()
    else:
        library.finish()
        sair = "S"

    os.system("pause"
              "")

