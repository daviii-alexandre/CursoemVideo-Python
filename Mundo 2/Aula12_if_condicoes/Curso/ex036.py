# Simulação de compra de Imóvel

from time import sleep
casaValor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casaValor / (anos * 12)
if prestacao <= (salario * (30 / 100)):
    print('\033[33mANALISANDO...\033[0m')
    sleep(2)
    print('\033[1;32m<SIMULAÇÃO VÁLIDA!>\033[0m Prosseguindo com os dados da aquisição...')
    sleep(1)
    print('-' * 40)
    print(f'Valor do imóvel: R${casaValor:.2f}\nQt. Meses: {anos * 12} meses\nValor das Prestações: R${prestacao:.2f}/mês')
    print('-' * 40)
elif prestacao > (salario * (30 / 100)):
    print('\033[33mANALISANDO...\033[0m')
    sleep(2)
    print('\033[1;31mSIMULAÇÃO INVÁLIDA!\033[0m O valor das prestações excede 30% do salário do comprador.\033[0m')