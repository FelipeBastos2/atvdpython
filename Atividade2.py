def analisar_frase(frase):
    # Remove espaços extras e divide a frase em palavras
    palavras = frase.strip().split()
    
    # Conta o número de caracteres
    caracteres = len(frase.replace(" ", ""))
    
    # Conta o número de vogais
    vogais = sum(1 for letra in frase.lower() if letra in 'aeiou')
    
    # Calcula os percentuais e médias
    percentual_vogais = (vogais / caracteres) * 100 if caracteres > 0 else 0
    numero_palavras = len(palavras)
    media_caracteres_por_palavra = caracteres / numero_palavras if numero_palavras > 0 else 0
    
    # Exibe os resultados
    print(f"Quantidade de caracteres: {caracteres}")
    print(f"Percentual de vogais: {percentual_vogais:.2f} %")
    print(f"Sua frase contém: {numero_palavras} palavras.")
    print(f"Em média temos {media_caracteres_por_palavra:.2f} caracteres por palavra.")

# Entrada
frase = input("Digite uma frase: ")
analisar_frase(frase)
