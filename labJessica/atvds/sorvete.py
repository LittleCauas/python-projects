def funcaoSorvete(s0, v, t):
    return s0 + (v * t)

posicaoInicial = float(input("Posição inical(km): "))
velocidade = float(input("Velocidade(km/h): "))
tempo = float(input("Tempo(hora): "))

print("Posição final é de: ", funcaoSorvete(posicaoInicial, velocidade, tempo))