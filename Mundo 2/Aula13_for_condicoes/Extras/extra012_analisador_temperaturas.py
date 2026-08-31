maior = ""
menor = ""
soma = 0
qt_temp = int(input("Quantidade de Temperaturas: "))
for verifica in range(1, qt_temp + 1):
    temp = float(input("Digite uma temperatura (ºC): "))
    soma += temp
    if temp <= 0:
        print("Status: \033[34mCONGELANTE\033[m")
    elif temp > 0 and temp <= 15:
        print("Status: \033[36mFRIA\033[m")
    elif temp >= 16 and temp <= 25:
        print("Status: \033[32mAMENA\033[m")
    elif temp > 25:
        print("Status: \033[33mQUENTE\033[m")
    if verifica == 1:
        maior = temp
        menor = temp
    elif temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
media = soma / qt_temp
print(f"A média das temperaturas é: \033[35m{media:.2f}ºC\033[m")
print(f"A maior temperatura é \033[33m{maior}ºC\033[m e a menor é \033[34m{menor}ºC\033[m")