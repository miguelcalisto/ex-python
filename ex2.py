
comprimento = float(input("Comprimento da cozinha (m): "))
largura = float(input("Largura da cozinha (m): "))
altura = float(input("Altura da cozinha (m): "))
area_paredes = 2 * altura * (comprimento + largura)
caixas = area_paredes / 1.5
print(f"Quantidade de caixas de azulejos: {caixas:.0f}")
