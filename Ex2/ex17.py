# 17. Soma entre n1 e n2
def soma_inteiros(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    return sum(range(n1, n2 + 1))

def exercicio17():
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    print(f"Soma: {soma_inteiros(n1, n2)}")
