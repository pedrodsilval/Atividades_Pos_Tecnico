import requests

url = "https://restcountries.com/v3.1/name/brazil"
resposta = requests.get(url)
dados = resposta.json()

# Pegando o primeiro (e único) item da lista retornada
pais = dados[0]

nome = pais["name"]["common"]
capital = pais["capital"][0]
populacao = pais["population"]

print(f"Nome do país: {nome}")
print(f"Capital: {capital}")
print(f"População: {populacao} habitantes")