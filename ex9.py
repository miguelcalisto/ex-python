
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or b == c or a == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Forma um triângulo {tipo}")
else:
    print("Não forma um triângulo")
