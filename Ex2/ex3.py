
aptos = 0

while True:
    nome = input("Nome (vazio para sair): ")
    if nome == "":
        break
    sexo = input("Sexo (M/F): ")
    idade = int(input("Idade: "))
    saude = input("Está saudável? (S/N): ")

    if sexo == "M" and idade >= 18 and saude == "S":
        print(nome, "está apto.")
        aptos += 1
    else:
        print(nome, "não está apto.")

print("Total de aptos:", aptos)
