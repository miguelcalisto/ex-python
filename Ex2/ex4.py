
numeros = []

for i in range(15):
    num = float(input("Digite um número: "))
    numeros.append(num)

for i in range(15):
    if numeros[i] < 0:
        print("Número negativo na posição", i)
