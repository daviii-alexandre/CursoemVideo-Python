estoque = 10
while estoque > 0:
    retirada = int(input("Quantas unidades deseja comprar? "))
    if retirada > estoque:
        print("\033[33mA quantidade de unidades retiradas excede a quantidade de produtos no estoque\033[m")
        continue
    estoque -= retirada
    print(f"Unidades restantes: {estoque}")
    print("-" * 30)
if estoque == 0:
    print("\033[31mESTOQUE ESGOTADO\033[m")