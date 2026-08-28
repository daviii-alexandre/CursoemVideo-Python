# Grupo de Maioridade 

from datetime import date
maior_idade = 0
menor_idade = 0
for pessoas in range (1, 8):
    ano = int(input(f"Ano de nascimento da {pessoas}ª pessoa: "))
    if (date.today().year - ano) >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print("-" * 30)
print(f"""Das 7 pessoas:
- \033[1;32m{maior_idade}\033[0m são \033[32mMAIORES DE IDADE\033[0m
- \033[1;35m{menor_idade}\033[0m são \033[35mMENORES DE IDADE\033[0m""")
print("-" * 30)