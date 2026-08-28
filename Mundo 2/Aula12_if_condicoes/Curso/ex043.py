# Calculadora de IMC

peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
IMC = peso / (altura ** 2)
print(f"Seu IMC é de {IMC:.2f}.")
if IMC < 18.5:
    print("Você está \033[1;31mABAIXO DO PESO!\033[0m")
elif IMC >= 18.5 and IMC < 25:
    print("PARABÉNS!!! você está no \033[1;32mPESO IDEAL!\033[0m")
elif IMC >= 25 and IMC < 30:
    print("Você está com \033[1;35mSOBREPESO\033[0m")
elif IMC >= 30 and IMC < 40:
    print('CUIDADO! Você está atingindo a \033[1;33mOBESIDADE\033[0m')
elif IMC >= 40:
    print("\033[1;31mATENÇÃO!!!\033[0m você está com \033[1;31mOBESIDADE MÓRBIDA\033[0m")