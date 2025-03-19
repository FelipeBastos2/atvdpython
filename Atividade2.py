def analisar_frase(frase):
    palavras = frase.strip().split()
    
    caracteres = len(frase.replace(" ", ""))
    
    vogais = sum(1 for letra in frase.lower() if letra in 'aeiou')
    
    percentual_vogais = (vogais / caracteres) * 100 if caracteres > 0 else 0
    numero_palavras = len(palavras)
    media_caracteres_por_palavra = caracteres / numero_palavras if numero_palavras > 0 else 0
    
    print(f"Quantidade de caracteres: {caracteres}")
    print(f"Percentual de vogais: {percentual_vogais:.2f} %")
    print(f"Sua frase contém: {numero_palavras} palavras.")
    print(f"Em média temos {media_caracteres_por_palavra:.2f} caracteres por palavra.")

frase = input("Digite uma frase: ")
analisar_frase(frase)
