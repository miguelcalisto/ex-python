
def esta_contida(str1, str2):
    # Verifica qual é a menor e a maior
    if len(str1) < len(str2):
        menor = str1
        maior = str2
    else:
        menor = str2
        maior = str1

    # Verifica se a menor está contida na maior
    if menor in maior:
        return 1
    else:
        return 0

# Programa principal
string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")

resultado = esta_contida(string1, string2)

if resultado == 1:
    print("A menor palavra está contida na maior.")
else:
    print("A menor palavra NÃO está contida na maior.")
