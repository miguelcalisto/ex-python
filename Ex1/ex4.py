
combustivel = float(input("Valor do combustível por litro: R$ "))
inicio = float(input("Odômetro no início do dia (km): "))
fim = float(input("Odômetro no final do dia (km): "))
litros = float(input("Litros consumidos: "))
receita = float(input("Valor recebido dos passageiros: R$ "))

km_rodado = fim - inicio
consumo = km_rodado / litros
lucro = receita - (litros * combustivel)

print(f"Média de consumo: {consumo:.2f} km/l")
print(f"Lucro líquido do dia: R$ {lucro:.2f}")
