genero = input("Qual seu gênero de filme favorito? (ação / comédia / terror): ").strip().lower()

# Lógica de recomendação
if genero == "ação":
    recomendacao = "Mad Max: Estrada da Fúria"
elif genero == "comédia":
    recomendacao = "Superbad: É Hoje"
elif genero == "terror":
    recomendacao = "Invocação do Mal"
else:
    recomendacao = "Gênero não reconhecido. Assista 'De Volta para o Futuro'!"

# Salvando a recomendação
with open("recomendacoes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Gênero escolhido: {genero.capitalize()}\n")
    arquivo.write(f"Filme recomendado: {recomendacao}\n")

print("Sua recomendação foi gerada e salva no arquivo recomendacoes.txt!")