
menor_impar = None

while True:
    n = int(input("Digite um número (negativo para sair): "))
    if n < 0:
        break
    if n % 2 != 0:
        if menor_impar is None or n < menor_impar:
            menor_impar = n

if menor_impar is None:
    print("Nenhum número ímpar foi informado.")
else:
    print(f"Menor número ímpar: {menor_impar}")
