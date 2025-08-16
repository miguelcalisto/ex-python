
mensalidade = float(input("Digite o valor da mensalidade: R$ "))
percentual = float(input("Digite o percentual de reajuste (%): "))
novo_valor = mensalidade * (1 + percentual / 100)
print(f"Novo valor da mensalidade: R$ {novo_valor:.2f}")
