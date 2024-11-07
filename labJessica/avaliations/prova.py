#Aluno 1: Cauã Florentino da Silva
#Aluno 2: Héric Maravai Simão
#Turma: 2-54

def calcular_gorjeta(valor):
    return valor * 0.10

pedidos = []
valor_total = 0

while True:
    descricao = input("Informe a descrição do produto: ")
    valor = float(input("Informe o valor do produto em R$: "))
    quantidade = int(input("Informe a quantidade: "))

    pedidos.append({'descricao': descricao, 'valor': valor, 'quantidade': quantidade, 'total_item': valor_total})

    valor_total += valor * quantidade

    opco = input("Deseja continuar? (S/N): ")
    print(f"")

    if opco.lower() == "n":
        break

gorjeta = calcular_gorjeta(valor_total)

totalGorjeta = valor_total + gorjeta

print("Os pedidos foram: ", pedidos)
print(f"")
print(f"O valor sem a gorjeta ficou: ", valor_total)
print(f"")
print(f"Total dos Pedidos: R$", totalGorjeta)
print(f"")
print(f"Gorjeta (10%): R$", gorjeta)