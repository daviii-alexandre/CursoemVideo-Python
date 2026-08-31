ultimo = 1
penultimo = 0
novo = 0
limite = int(input("Número Limite: "))
if limite == 0:
    print('')
elif limite == 1:
    print("0")
else:
    print(f"{penultimo} - {ultimo} ", end="")
for sequencia in range(2, limite):
    novo = penultimo + ultimo
    print(f"- {novo}", end=" ")
    penultimo = ultimo
    ultimo = novo