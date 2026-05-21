from pathlib import Path

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


downloads = Path.home() / "Downloads"

arquivo = open(downloads / "resultados.txt", "w", encoding="utf-8")


for ciclo in range(ciclos):

    print(f"\n===== CICLO {ciclo + 1} =====")

    arquivo.write(f"\n===== CICLO {ciclo + 1} =====\n")

    for i, (x, y) in enumerate(dados):

        soma = 0

        for j in range(len(x)):

            soma += x[j] * w[j]

        saida = ativacao(soma)

        erro = y - saida

        print(f"\nExemplo {i + 1}")
        print(f"Entrada: {x}")
        print(f"Saída esperada: {y}")
        print(f"Saída encontrada: {saida}")
        print(f"Erro: {erro}")

        arquivo.write(f"\nExemplo {i + 1}\n")

        arquivo.write(f"Entrada: {x}\n")

        arquivo.write(f"Saída esperada: {y}\n")

        arquivo.write(f"Saída encontrada: {saida}\n")

        arquivo.write(f"Erro: {erro}\n")

        for j in range(len(w)):

            w[j] = w[j] + alpha * erro * x[j]

        print(f"Pesos atualizados: {w}")

        arquivo.write(f"Pesos atualizados: {w}\n")


arquivo.close()

print("\nTreinamento finalizado.")

print("Pesos finais:", w)

print("\nArquivo salvo em Downloads.")