# 19. Contar vogais em string
def exercicio19():
    s = input("Digite uma string: ")
    if not s:
        print("String vazia!")
        return
    count = sum(eh_vogal(c) for c in s)
    print(f"Número de vogais: {count}
