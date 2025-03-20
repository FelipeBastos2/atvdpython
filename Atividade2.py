def analisar_frase(frase):
    palavras = frase.split()
    caracteres = 0
    for letra in frase:
        if letra != " ":
            caracteres += 1
    vogais = 0
    for letra in frase.lower():
        if letra in 'aeiou':
            vogais += 1

    if caracteres > 0:
        percentual_vogais = (vogais / caracteres) * 100
    else:
        percentual_vogais = 0

    numero_palavras = len(palavras)

    if numero_palavras > 0:
        media_caracteres_por_palavra = caracteres / numero_palavras
    else:
        media_caracteres_por_palavra = 0
    print("Quantidade de caracteres:", caracteres)
    print("Percentual de vogais: {:.2f}%".format(percentual_vogais))
    print("Sua frase contém:", numero_palavras, "palavras.")
    print("Em média temos {:.2f} caracteres por palavra.".format(media_caracteres_por_palavra))

frase = input("Digite uma frase: ")
analisar_frase(frase)
