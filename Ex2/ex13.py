# 13. Maior por linha e menor por coluna
def exercicio13():
    matriz = [[int(input(f"[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
    for i, linha in enumerate(matriz):
        print(f"Linha {i} - maior elemento: {max(linha)}")
    for j in range(5):
        col = [matriz[i][j] for i in range(5)]
        print(f"Coluna {j} - menor elemento: {min(col)}")
