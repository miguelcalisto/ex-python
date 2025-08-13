
x = int(input("Digite o valor a ser contado: "))
contador = 0

while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n == x:
        contador += 1

print(f"O valor {x} apareceu {contador} vezes.")
