# 14. Soma das diagonais principais
def exercicio14():
    matriz1 = [[int(input(f"Matriz 1 [{i}][{j}]: ")) for j in range(4)] for i in range(4)]
    matriz2 = [[int(input(f"Matriz 2 [{i}][{j}]: ")) for j in range(4)] for i in range(4)]
    soma1 = sum(matriz1[i][i] for i in range(4))
    soma2 = sum(matriz2[i][i] for i in range(4))
    print("Somas iguais" if soma1 == soma2 else "Somas diferentes")
