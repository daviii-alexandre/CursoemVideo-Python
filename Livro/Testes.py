menor = ""
maior = ""
qt = 1
n = int(input("Digite um valor: "))
soma = n
pergunta = str(input("Deseja inserir mais um valor? [S/N] ")).strip().upper()
maior = n       #Transforma o primeiro valor digitado no maior valor automaticamente
menor = n       #Transforma o primeiro valor digitado no menor valor automaticamente
print("-" * 50)
while pergunta != "N":
    n = int(input("Digite um valor: "))
    pergunta = str(input("Deseja inserir mais um valor? [S/N] ")).strip().upper()
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    qt += 1
    soma += n
    print("-" * 50)
media = soma / qt
print(f"A \033[35mMÉDIA\033[m dos valores lidos é \033[35m{media}\033[m.\nO \033[36mMENOR\033[m valor é \033[36m{menor}\033[m e o \033[33mMAIOR\033[m é \033[33m{maior}\033[m.")