import requests

# Fazendo a requisição na API da AwesomeAPI
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()

# Acessando as chaves do dicionário para pegar apenas o valor (bid)
valor_dolar = dados["USDBRL"]["bid"]

print(f"Cotação atual do Dólar: R$ {valor_dolar}")