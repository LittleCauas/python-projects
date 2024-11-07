def meses():
    pesos = 0
    meses_lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho','julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    for mes in meses_lista:
        peso = float(input(f"Informe seu peso no mês de {mes} em Kg: "))
        pesos[mes] = peso

    for i in range(len(meses_lista) - 1):
        mes_atual = meses_lista[i]
        proximo_mes = meses_lista[i + 1]
        resultado = pesos[mes_atual] - pesos[proximo_mes]

        if pesos[proximo_mes] > pesos[mes_atual]:
            print(f"O seu peso aumentou de {mes_atual} para {proximo_mes}: {abs(resultado)} Kg.")
        elif pesos[proximo_mes] < pesos[mes_atual]:
            print(f"O seu peso diminuiu de {mes_atual} para {proximo_mes}: {abs(resultado)} Kg.")
        else:
            print(f"Seu peso não mudou de {mes_atual} para {proximo_mes}.")
meses()
