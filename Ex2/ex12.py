# 12. Menor e maior em matriz
def exercicio12():
    matriz = []
    menor = float('inf')
    maior = float('-inf')
    pos_menor = pos_maior = (0, 0)
    for i in range(10):
        linha = []
        for j in range(10):
            val = float(input(f"[{i}][{j}]: "))
            linha.append(val)
            if val < menor:
                menor = val
                pos_menor = (i, j)
            if val > maior:
                maior = val
                pos_maior = (i, j)
        matriz.append(linha)
    print(f"Menor: {menor} em {pos_menor}, Maior: {maior} em {pos_maior}")
