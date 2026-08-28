# Maior e Menor Número da Sequência

maior_peso = 0
menor_peso = 0
for pessoas in range(1, 6):
    peso = float(input(f"Peso(Kg) da {pessoas}ª: "))
    if pessoas == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f"A pessoa com \033[1;33mMAIOR PESO\033[0m pesa \033[33m{maior_peso}Kg\033[0m")
print(f"A pessoa com \033[1;34mMENOS PESO\033[0m pesa \033[34m{menor_peso}Kg\033[0m")