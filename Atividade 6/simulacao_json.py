import json

# Cria um dicionário simulando o envio de uma pergunta para uma IA [cite: 386]
dados_ia = {
    "usuario": "Pedro",
    "pergunta": "O que é machine learning?",
    "status": "processando"
}

# Exibe o JSON formatado utilizando a biblioteca json [cite: 387]
json_formatado = json.dumps(dados_ia, indent=4, ensure_ascii=False)
print("Payload de envio para a IA:")
print(json_formatado)