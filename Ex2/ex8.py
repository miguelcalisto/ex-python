
palavra = input("Digite uma palavra: ")

inverso = ""

for i in range(len(palavra)-1, -1, -1):
    inverso += palavra[i]

if palavra == inverso:
    print("É palíndromo")
else:
    print("Não é palíndromo")
