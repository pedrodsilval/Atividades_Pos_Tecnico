# Solicita uma palavra ao usuário [cite: 370]
palavra = input("Digite uma palavra para análise: ").strip().lower()

positivas = ["feliz", "alegre", "bom", "ótimo", "excelente"]
negativas = ["triste", "ruim", "péssimo", "horrível", "bravo"]

# Classifica o sentimento [cite: 371]
if palavra in positivas:
    sentimento = "Positivo"
elif palavra in negativas:
    sentimento = "Negativo"
else:
    sentimento = "Neutro"

# Exibe o resultado da análise [cite: 372]
print(f"Sentimento identificado: {sentimento}")