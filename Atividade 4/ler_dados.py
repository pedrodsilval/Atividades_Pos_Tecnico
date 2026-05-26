try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo 'dados.txt' não foi encontrado. Crie ele primeiro!")