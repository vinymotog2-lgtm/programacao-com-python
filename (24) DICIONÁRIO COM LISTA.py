
personagem = {
    "nome": "Arqueiro",
    "nivel": 1,
    "inventario": [] # Lista dentro do dicionario
}
iten1 = input("Digite um item")
iten2 = input("Digite outro item")
personagem{"inventario"}.append("Espada")
personagem{"inventario"}.append("Poção")
personagem{"inventario"}.append("Flecha")
print("Nome", personagem ["nome"])
print("Nome", personagem ["classe"])
print("Nome", personagem ["nivel"])
print("---Inventario---")
for item in personagem["inventario"]:
    print("-", item)