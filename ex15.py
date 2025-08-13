
print("Números que satisfazem a condição:")

for num in range(1000, 10000):
    parte1 = num // 100
    parte2 = num % 100
    soma = parte1 + parte2
    if soma * soma == num:
        print(num)
