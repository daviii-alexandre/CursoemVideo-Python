# Detector de Palíndromo

frase = str(input("Digite uma frase: ")).strip().upper().replace(" ", "")
print(f"O inverso da frase {frase} é {frase[::-1]}")
if frase == frase[::-1]:
    print("Sua frase \033[1;34mÉ UM PALÍNDROMO!\033[0m")
else:
    print("Sua frase \033[1;31mNÃO É UM PALÍNDROMO!\033[0m")