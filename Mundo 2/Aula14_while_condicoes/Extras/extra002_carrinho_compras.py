from time import sleep
produto = float(input("Valor do produto: R$ "))
soma = produto
add = str(input("Deseja adicionar mais produtos? [S/N] ")).strip().upper()
while add == "S":
    produto = float(input("Valor do produto: R$ "))
    add = str(input("Deseja adicionar mais produtos? [S/N] ")).strip().upper()
    soma += produto
print("\033[1;36mCalculando compra...\033[m")
sleep(1)
print("-" * 20)
print(f"Valor final: \033[32mR$ {soma:.2f}\033[m")
print("-" * 20)