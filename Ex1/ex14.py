
maior = segundo = float('-inf')

for _ in range(10):
    n = int(input("Digite um número: "))
    if n > maior:
        segundo = maior
        maior = n
    elif n > segundo:
        segundo = n

print(f"Maior número: {maior}")
print(f"Segundo maior número: {segundo}")
