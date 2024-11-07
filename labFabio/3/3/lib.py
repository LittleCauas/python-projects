jogadores = []

def adicionar(nome):
    jogadores.append(nome)
def visualizar():
    for i in jogadores:
        print("Time: ", i)
def pesquisar(camisa):
    print("Jogador: ", jogadores[camisa - 1])