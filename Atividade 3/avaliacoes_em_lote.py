palavras_positivas = ["bom", "ótimo", "excelente"]
contador = 0

print("Digite palavras para análise.")
print("DICA: Digite 'sair' para finalizar o programa.\n")

# Loop para receber várias palavras
while True:
    palavra = input("Digite uma palavra: ").strip().lower()
    
    if palavra == "sair":
        break
        
    # Se a palavra estiver na lista de positivas, aumenta o contador
    if palavra in palavras_positivas:
        contador += 1

# Exibe o total ao final
print(f"\nAnálise concluída!")
print(f"Total de palavras positivas identificadas: {contador}")