# 16. Elemento minimax
def exercicio16():
    matriz = [[int(input(f"[{i}][{j}]: ")) for j in range(10)] for i in range(10)]
    maior = float('-inf')
    pos_maior = (0, 0)
    for i in range(10):
        for j in range(10):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = (i, j)
    linha = matriz[pos_maior[0]]
    minimax = min(linha)
    print(f"Elemento minimax: {minimax} na linha {pos_maior[0]}")
