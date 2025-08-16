# 11. Contar pares, ímpares e zeros
def exercicio11():
    matriz = []
    pares = impares = zeros = 0
    for i in range(5):
        linha = []
        for j in range(5):
            val = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(val)
            if val == 0:
                zeros += 1
            elif val % 2 == 0:
                pares += 1
            else:
                impares += 1
        matriz.append(linha)
    print(f"Pares: {pares}, Ímpares: {impares}, Zeros: {zeros}")
