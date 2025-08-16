
texto = input("Digite uma palavra: ")
n = int(input("Quantas letras deseja remover do final? "))

nova = texto[0:len(texto)-n]
print("Resultado:", nova)
