pesoJan = float(input(f"Infome seu peso no mês de janeiro em Kg: "))
pesoFev = float(input(f"Infome seu peso no mês de fevereiro em Kg: "))

result1 = pesoJan - pesoFev

if pesoFev > pesoJan:
    print(f"O seu peso diminuiu em: ", abs(result1))
if pesoFev < pesoJan:
    print(f"O seu peso aumentou em: ", abs(result1))
else:
    print(f"Seu peso não mudou. ")
