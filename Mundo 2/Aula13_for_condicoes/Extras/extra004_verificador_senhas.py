# Verificador de Senhas

letras = False
numeros = False
senha = input("Digite uma senha: ")
for verifica in senha:
     if verifica.isdigit():
          numeros = True
     if verifica.isupper():
          letras = True
if numeros and letras:
     print(f"\033[32mSenha Forte\033[0m")
elif numeros:
     print(f"\033[33mSenha fraca!\033[0m A senha precisa conter uma \033[35mLETRA MAIÚSCULA\033[0m")
elif letras:
     print(f"\033[33mSenha fraca!\033[0m A senhah precisa conter um \033[1;35mNÚMERO\033[0m")
else:
     print(f"\033[31mSenha muito fraca!!!\033[0m A senha precisa conter um \033[35mNÚMERO\033[0m e uma \033[35mLETRA MAIÚSCULA\033[0m")