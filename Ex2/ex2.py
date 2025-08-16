# 2. Dicionário com médias
def exercicio2():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (vazio para sair): ")
        if nome == "":
            break
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        alunos[nome] = (n1 + n2) / 2

    busca = input("Digite o nome do aluno para ver a média: ")
    print(f"Média de {busca}: {alunos.get(busca, 'Aluno não encontrado')}")
