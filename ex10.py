
altura = float(input("Altura (m): "))
peso = float(input("Peso (kg): "))
sexo = input("Sexo (M/F): ").upper()

if sexo == 'M':
    ideal = 72.7 * altura - 58
else:
    ideal = 62.1 * altura - 44.7

diferenca = peso - ideal

print(f"Peso ideal: {ideal:.2f} kg")
if diferenca > 0:
    print(f"Está acima do peso ideal por {diferenca:.2f} kg")
else:
    print(f"Está abaixo do peso ideal por {-diferenca:.2f} kg")
