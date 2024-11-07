from operator import is_not

nomes = []

while True:
    nome = input("Nome: ")
    nomes.append(nome)
    continuar = input("Deseja continuar S/N: ")

    if continuar.lower() == "n":
        break
    else:
        continue

print("## Lista de nomes ##")
for i in nomes:
    print("- ", i)
