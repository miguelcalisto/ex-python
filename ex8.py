
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

largura = abs(x2 - x1)
altura = abs(y2 - y1)
area = largura * altura

print(f"Área do retângulo: {area:.2f} m²")
