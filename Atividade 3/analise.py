# Solicita uma palavra
palavra = input("Digite uma palavra para análise: ").strip().lower()

# Listas de palavras para comparação
palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "legal"]
palavras_negativas = ["ruim", "péssimo", "horrível", "chato", "triste"]

# Classificação
if palavra in palavras_positivas:
    print("Classificação: Positivo")
elif palavra in palavras_negativas:
    print("Classificação: Negativo")
else:
    print("Classificação: Neutro")