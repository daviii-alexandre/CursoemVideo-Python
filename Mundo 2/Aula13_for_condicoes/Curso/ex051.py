# Progressão Aritmética

t1 = int(input("Qual o primeiro termo? "))
razao = int(input("Razão: "))
decimo = t1 + (10 - 1) * razao
for pa in range (t1, decimo, razao):
    print(f"{pa} ", end=' 🠒 ')
print("CABÔ")