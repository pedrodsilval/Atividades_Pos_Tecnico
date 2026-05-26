# Solicita o gênero de filme ao usuário
genero = input("Digite um gênero de filme (ação, comédia ou terror): ").strip().lower()

# Estrutura condicional para recomendação
if genero == "ação":
    print("Recomendação: 'Mad Max: Estrada da Fúria' - Muita adrenalina e perseguições!")
elif genero == "comédia":
    print("Recomendação: 'Superbad' - Para dar boas risadas!")
elif genero == "terror":
    print("Recomendação: 'Invocação do Mal' - Prepare-se para os sustos!")
else:
    print("Ops! Gênero não reconhecido. Tente digitar ação, comédia ou terror.")