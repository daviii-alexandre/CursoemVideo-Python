usuario = "daviii_alexandre"
senha = "0319"
resposta1 = str(input("Usuário: "))
resposta2 = str(input("Senha: "))
while resposta1 != usuario  or resposta2 != senha:
    if resposta1 != usuario:
        print("\033[31mCREDENCIAIS INVÁLIDAS!\033[m\nNome de \033[35mUSUÁRIO\033[m incorreto")
        print("-" * 20)
    elif resposta2 != senha:
        print("\033[31mCREDENCIAIS INVÁLIDAS!\033[m\n\033[35mSENHA incorreta\033[m")
        print("-" * 20)
    resposta1 = str(input("Usuário: "))
    resposta2 = str(input("Senha: "))
print("\033[32mACESSO LIBERADO\033[m")