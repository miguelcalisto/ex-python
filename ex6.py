
disciplina = input("Nome da disciplina: ")
carga_horaria = int(input("Carga horária total: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
faltas = int(input("Número de faltas: "))

media = (nota1 + nota2 + nota3) / 3
frequencia = (1 - faltas / carga_horaria) * 100

print(f"\nDisciplina: {disciplina}")
print(f"Média final: {media:.2f}")
print(f"Frequência: {frequencia:.1f}%")

if frequencia < 75:
    print("Resultado: Reprovado por frequência")
elif media >= 6.0:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")
