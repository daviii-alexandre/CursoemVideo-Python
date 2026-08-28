# Gerenciador de Pagamentos

valorProduto = float(input(f"Valor do produto: "))
print('-'*30)
print(f"\033[33m     OPÇÕES DE PAGAMENTO\033[0m")
print("1. \033[34mDinheiro/Cheque/Pix\033[0m")
print("2. \033[34mCartão (Débito)\033[0m")
print("3. \033[34mCartão (Crédito)\033[0m")
print('-'*30)
pagamento = int(input("Selecione a opÇão de pagamento desejada: "))
if pagamento == 1:
    desconto = valorProduto * (10 / 100)
    valorFinal = valorProduto - desconto
    print(f"\033[32mDesconto: -{desconto}R$\033[0m")
    print(f"Valor final do produto: \033[34mR${valorFinal:.2f}\033[0m")
elif pagamento == 2:
    desconto = valorProduto * (5 /100)
    valorFinal = valorProduto - desconto
    print(f"\033[32mDesconto: -{desconto}R$\033[0m")
    print(f"Valor final do produto: \033[34mR${valorFinal:.2f}\033[0m")
elif pagamento == 3:
    parcelas = int(input("Quantidade de parcelas: "))
    if parcelas == 2:
        valorParcelas = valorProduto / 2
        print(f"Valor das Parcelas: \033[33m2x R${valorParcelas:.2f}\033[0m")
    elif parcelas > 2:
        juros = valorProduto * (20 / 100)
        valorJuros = valorProduto + juros
        valorParcelas = valorJuros / parcelas
        print(f"Valor Final do Produto: \033[34mR${valorJuros:.2f}\033[0m")
        print(f"Valor das Parcelas: \033[33m{parcelas}x de R${valorParcelas:.2f}\033[0m")
        print("\033[31mTaxa de Juros = 20%\033[0m")