def convercao(valor, cotacao):
    return valor / cotacao

cotacaoEuro = float(input("Informe a cotação do euro: "))
cotacaoDolar = float(input("Informe a cotação do dolár: "))
valor = float(input("Informe o valor que quer converter (R$): "))

print("Valor convertido em dolar é de $", convercao(valor, cotacaoDolar))
print("Valor convertido em euro é de €", convercao(valor, cotacaoEuro))