import requests

url = "https://api.github.com"
resposta = requests.get(url)

# Convertendo a resposta para um dicionário Python (JSON)
dados = resposta.json()

print("--- Dados retornados pela API do GitHub ---")
print(dados)