lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata-Frita")

for comida in range(0, len(lanche)):
    print(lanche[comida])

for comida in lanche:
    print(f"Vou comer {comida}")

for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")

print("Nossa, comi pra caramba...")