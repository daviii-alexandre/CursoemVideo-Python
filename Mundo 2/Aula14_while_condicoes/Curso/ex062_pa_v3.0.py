from time import sleep
t1 = int(input("Qual é o primeiro termo? "))
razao  = int(input("Qual é a razão? "))
cont = 1
atual = t1
texto = ""
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{atual} -> ", end='')
        atual += razao
        cont += 1
    print("FIM")
    print("-" * 50)
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("\033[1;35mCalculando Termos...\033[m")
sleep(2)
print("×" * 50)
print(f"\033[34mProgressão Final: {total} termos mostrados\033[m")
print("×" * 50)