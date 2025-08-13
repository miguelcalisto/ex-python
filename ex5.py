
altura = float(input("Altura da parede (m): "))
largura = float(input("Largura da parede (m): "))
preco_galao = float(input("Preço de cada galão de tinta: R$ "))

area = altura * largura
galoes = area / 2
total = (int(galoes) + 1) * preco_galao

print(f"Galões necessários: {int(galoes) + 1}")
print(f"Preço total: R$ {total:.2f}")
