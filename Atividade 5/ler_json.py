import json

try:
    # Abrindo o arquivo físico questao5.json
    with open("questao5.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo) # json.load transforma o arquivo em dicionário Python

    # Acessando as chaves
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")

except FileNotFoundError:
    print("Erro: O arquivo 'questao5.json' não foi encontrado na pasta.")