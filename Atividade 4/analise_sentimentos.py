palavra = input("Digite uma palavra para análise: ").strip().lower()

# Lógica de classificação
if palavra in ["bom", "ótimo", "excelente"]:
    sentimento = "Positivo"
elif palavra in ["ruim", "péssimo", "horrível"]:
    sentimento = "Negativo"
else:
    sentimento = "Neutro ou não mapeado"

# Salvando o resultado
with open("sentimentos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Palavra analisada: '{palavra}'\n")
    arquivo.write(f"Sentimento detectado: {sentimento}\n")

print("Análise concluída e salva em sentimentos.txt!")