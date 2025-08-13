
eleitores = int(input("Número de eleitores: "))
brancos = int(input("Votos brancos: "))
nulos = int(input("Votos nulos: "))
validos = int(input("Votos válidos: "))

print(f"Brancos: {(brancos/eleitores)*100:.2f}%")
print(f"Nulos: {(nulos/eleitores)*100:.2f}%")
print(f"Válidos: {(validos/eleitores)*100:.2f}%")
