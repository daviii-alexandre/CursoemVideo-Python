estoque = ("Arroz", 22, "Feijão", 30, "Cuscuz", 10, "Tapioca", 40, "Açucar", 8)
for produto in range(1, len(estoque), 2):
    if estoque[produto] < 25:
        print(f"O produto {estoque[produto - 1]} está com pouco estoque")
    else:
        print(f"O produto {estoque[produto - 1]} está com o estoque está cheio")