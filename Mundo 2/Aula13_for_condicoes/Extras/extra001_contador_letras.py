# Contador de letras

palavra = str(input("Digite uma palavra: ")).strip()
for letra in palavra:
    print(letra)
print(f"A palavra {palavra} possui {len(palavra)} letras")