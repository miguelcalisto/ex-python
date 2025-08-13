
inicio = int(input("Início do intervalo de x: "))
fim = int(input("Fim do intervalo de x: "))

for x in range(inicio, fim + 1):
    y = 4 * x + 3
    print(f"x = {x}, y = {y}")
