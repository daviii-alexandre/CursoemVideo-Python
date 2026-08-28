# Tabuada 2.0

numero = int(input("Escolha a tabuada: "))
print("-"*30)
for tabuada in range(1, 11):
    multi = numero * tabuada
    print(f"{numero} x {tabuada} = {multi}")
print("-"*30)
