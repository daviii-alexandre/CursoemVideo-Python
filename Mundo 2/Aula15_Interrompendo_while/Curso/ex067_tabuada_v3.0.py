while True:
    print("-" * 30)
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")
    print("-" * 30)
    if n <= 0:
        print("PROGRAMA ENCERRADO. Volte sempre!")
        break