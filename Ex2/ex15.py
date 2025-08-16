# 15. Linha com menor soma
def exercicio15():
    matriz = [[int(input(f"[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
    somas = [sum(linha) for linha in matriz]
    menor = min(somas)
    for i, soma in enumerate(somas):
        if soma == menor:
            print(f"Linha {i} com soma {soma}")
