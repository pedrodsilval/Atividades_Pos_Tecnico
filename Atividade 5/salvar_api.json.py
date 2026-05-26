import requests
import json

# Consultando a API
cep = "42700000"
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

# Salvando a resposta no disco rígido
with open("dados_api.json", "w", encoding="utf-8") as arquivo:
    # json.dump escreve o dicionário diretamente no arquivo
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Sucesso! Os dados da API foram salvos no arquivo 'dados_api.json'.")