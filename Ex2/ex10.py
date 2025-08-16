
def cortar_palavra(palavra, letra):
    # Encontrar a posição da letra na palavra
    posicao = palavra.find(letra)

    # Se a letra foi encontrada
    if posicao != -1:
        # Cortar a palavra até a posição da letra
        return palavra[:posicao]
    else:
        # Se a letra não está na palavra, retorna a palavra inteira
        return palavra

# Programa principal
palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

resultado = cortar_palavra(palavra, letra)

print("Palavra cortada:", resultado)
