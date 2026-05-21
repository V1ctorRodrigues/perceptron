dados = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 1),
    ([1, 1], 1)
]

w = [0, 0]

alpha = 0.1

ciclos = 2
def ativacao(valor):

    if valor >= 0:
        return 1

    return 0