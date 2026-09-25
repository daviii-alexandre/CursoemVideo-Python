lista = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
vogais = "aeiou"
for nomes in lista:
    print(f"A palavra \033[1;35m{nomes.upper()}\033[m possui as vogais ", end="")
    for letra in nomes:
        if letra in vogais:
            print(f"\033[35m{letra}\033[m", end=" ")
    print()