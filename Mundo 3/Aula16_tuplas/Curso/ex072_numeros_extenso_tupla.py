numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
usuario = int(input("Digite um número: "))
while True:
    if usuario < 0 or usuario > 20:
        print("\033[31mResposta inválida!\033[m Escolha um número entre 0 e 20")
        print("-" * 30)
        usuario = int(input("Digite um número: "))
    else:
        print(f"Você escolheu o número \033[36m{numeros[usuario]}\033[m")
        break