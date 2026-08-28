# Analisador de Frase

letras = ""
espacos = ""
frase = str(input("Digite uma frase: ")).strip()
for caractere in frase:
    if caractere == " ":
        espacos += caractere
    else:
        letras += caractere
print(f"Sua frase possui {len(letras)} letras e {len(espacos)} espaços")
letras_maiusculas = letras.upper()
if letras_maiusculas == letras_maiusculas[::-1]:
    print(f"Sua frase também é um palíndromo, ou seja, é a mesma coisa de trás para frente")
else:
    print(f"Sua frase não é um palíndromo, pois ao contrário ela ficaria {letras[::-1]}")