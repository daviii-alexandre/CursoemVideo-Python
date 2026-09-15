usuario = "daviii_alexandre"
senha = "0319"
resposta_usuario = str(input("Usuário: "))
resposta_senha = str(input("Senha: "))
erros = 0
while erros < 2 and (resposta_usuario != usuario or resposta_senha != senha):
    print("\033[33mUSUÁRIO ou SENHA incorretos! Tente novamente.\033[m")
    resposta_usuario = str(input("Usuário: "))
    resposta_senha = str(input("Senha: "))
    erros += 1
if resposta_usuario == usuario and resposta_senha == senha:
    print("\033[32mACESSO PERMITIDO\033[m")
else:
    print("\033[31mACESSO BLOQUEADO\033[m")