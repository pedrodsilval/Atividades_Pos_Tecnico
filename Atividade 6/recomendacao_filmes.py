# Solicita o gênero favorito do usuário [cite: 376]
genero = input("Qual o seu gênero de filme favorito? (Ação/Comédia/Ficção): ").strip().lower()

# Recomenda um filme baseado na entrada 
if genero == "ação":
    recomendacao = "John Wick"
elif genero == "comédia":
    recomendacao = "Gente Grande"
elif genero == "ficção":
    recomendacao = "Interestelar"
else:
    recomendacao = "Vingadores (Gênero geral)"

# Exibe a recomendação na tela [cite: 378]
print(f"Filme recomendado para você: {recomendacao}")