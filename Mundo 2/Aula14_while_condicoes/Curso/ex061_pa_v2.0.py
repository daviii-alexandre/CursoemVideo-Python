t1 = int(input("Qual é o primeiro termo? "))
razao  = int(input("Qual é a razão? "))
cont = 1
atual = t1
texto = ""
while cont <= 10:
    texto += f"{atual} -> "
    atual += razao
    cont += 1
print(texto.rstrip('-> '))