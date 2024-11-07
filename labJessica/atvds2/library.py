import os

def finish():
    exibir_titulo("# Obrigado por utilizar nosso programa!")
    os.system("pause")

def sair():
    print()
    sair = input("Deseja sair do programa (S/N)? \n R: ")
    if sair.lower() == "s":
        finish()
    return sair

def separador():
    print()
    print("+---------------------------------------------------+")

def exibir_titulo(texto):
    os.system("cls")
    print(texto)

atendimentos = []

def adicionar(nome):
    atendimentos.append(nome)

def visualizar():
    for i in atendimentos: ##loop estrutura atendimento
        print("Nome: " , i)

def prox_senha():
    print("A próxima senha é: ", len(atendimentos) +1)

def disponiveis():
    print("Atendimentos disponíveis: ", 10-len(atendimentos))

def buscar(numero):
    if 1 <= numero <= len(atendimentos):
        print(f"Nome na posição {numero}: {atendimentos[numero - 1]}")
    else:
        print("Número inválido. Tente um número entre 1 e", len(atendimentos))
