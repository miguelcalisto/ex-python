def exercicio1():
    notas = []
    while True:
        nota = float(input("Digite uma nota (-1 para sair): "))
        if nota == -1:
            break
        notas.append(nota)

    print(f"a) Quantidade de valores lidos: {len(notas)}")
    print(f"b) Valores na ordem digitada: {notas}")
    print(f"c) Valores na ordem inversa: {list(reversed(notas))}")
    soma = sum(notas)
    media = soma / len(notas) if notas else 0
    print(f"d) Soma dos valores: {soma}")
    print(f"e) Média dos valores: {media}")
    acima = len([n for n in notas if n > media])
    print(f"f) Quantidade de valores acima da média: {acima}")
    ref = float(input("Digite um valor de referência: "))
    abaixo = len([n for n in notas if n < ref])
    print(f"g) Valores abaixo de {ref}: {abaixo}")
