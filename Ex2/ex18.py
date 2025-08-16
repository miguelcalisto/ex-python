# 18. Verificar vogal
def eh_vogal(c):
    return 1 if c.lower() in 'aeiou' else 0

def exercicio18():
    c = input("Digite um caractere: ")
    print("É vogal" if eh_vogal(c) else "Não é vogal")
