
pesoJan = float(input("Informe seu peso no mes de janeiro em Kg: "))
pesoFev = float(input("Informe seu peso no mes de fevereiro em Kg: "))

diferenca1 = pesoJan - pesoFev

if (pesoFev > pesoJan):
    print("Seu peso aumentou em: ", abs(diferenca1))

if(pesoJan > pesoFev):
    print("Seu peso diminuiu em: ", abs(diferenca1))

else:print("Seu peso permaneceu o mesmo!")

pesoMarc = float(input("Informe seu peso no mes de março em Kg: "))
pesoAbr = float(input("Informe seu peso no mes de abril em Kg: "))

diferenca2 = pesoMarc - pesoAbr

if (pesoAbr > pesoMarc):
    print("Seu peso aumentou em: ", abs(diferenca2))

if (pesoMarc > pesoAbr):
    print("Seu peso diminuiu em: ", abs(diferenca2))

else:
    print("Seu peso permaneceu o mesmo!")

pesoMaio = float(input("Informe seu peso no mes de maio em Kg: "))
pesoJun = float(input("Informe seu peso no mes de junho em Kg: "))

diferenca3 = pesoMaio - pesoJun

if (pesoJun > pesoMaio):
    print("Seu peso aumentou em: ", abs(diferenca3))

if (pesoMaio > pesoJun):
    print("Seu peso diminuiu em: ", abs(diferenca3))

else:
    print("Seu peso permaneceu o mesmo!")

pesoJul = float(input("Informe seu peso no mes de julho em Kg: "))
pesoAgo = float(input("Informe seu peso no mes de agosto em Kg: "))

diferenca3 = pesoJul - pesoAgo

if (pesoAgo > pesoJul):
    print("Seu peso aumentou em: ", abs(diferenca3))

if (pesoJul > pesoAgo):
    print("Seu peso diminuiu em: ", abs(diferenca3))

else:
    print("Seu peso permaneceu o mesmo!")




