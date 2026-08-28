vogais = 0      # Guarda o total de vogais
maisVogais = ""     # Palavra com mais vogais
vogaisNaPalavra = 0     # Quantas vogais têm na palavra
recordVogais = 0        # Quantidade de vogais da palavra recordista
qntPalavras = int(input("Quantas palavras? "))      # Pede a quantidade de palavras
for palavrasGeral in range(1, qntPalavras+1):       # Passa por todas as palavras
    palavra = str(input(f"{palavrasGeral}ª palavra: ")).strip().upper()     # Pede a palavra
    vogaisNaPalavra = 0     # Reseta a quantidade de vogais na palavra
    for caractere in palavra:       # Passa por todas as letras da cada palavra uma por uma
        if caractere in ["A", "E", "I", "O", "U"]:      # Verifica se têm vogal na palavra
            vogaisNaPalavra += 1        # Se tiver vogal, soma + 1 na quantidade de vogais na palavra
            vogais += 1     # Soma +1 na quantidade geral de vogais
    if palavrasGeral == 1:    # Verifica se é a primeira palavra e guarda maisVogais nela
        maisVogais = palavra        # Como é a primeira palavra, guarda ela como a que tem mais vogais
        recordVogais = vogaisNaPalavra      # Como é a primeira palavra, guarda ela como recordista em vogais
    else:
        if vogaisNaPalavra > recordVogais:      # Se não for a primeira palavra, compara as vogais da palavra atual com as da recordista (palavra anterior)
            maisVogais = palavra        # Se tiver mais vogais, a nova palavra passa ser a que tem mais vogais
            recordVogais = vogaisNaPalavra      # a nova palavra passa a ser a recordista

print(f"A palavra com mais vogais é {maisVogais}\nTotal de vogais: {vogais}")
