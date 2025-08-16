
palavra = input("Digite uma palavra: ")
letra1 = input("Letra a ser substituída: ")
letra2 = input("Nova letra: ")

nova = ""

for letra in palavra:
    if letra == letra1:
        nova += letra2
    else:
        nova += letra

print("Nova palavra:", nova)
