
texto = input("Digite uma palavra: ")
vogais = ""

for letra in texto:
    if letra in "aeiouAEIOU":
        vogais += letra

print("Vogais:", vogais)
