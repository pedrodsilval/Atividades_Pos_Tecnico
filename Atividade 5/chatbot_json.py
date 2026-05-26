import json

print("--- Chatbot JSON ---")
pergunta_usuario = input("Digite a sua pergunta: ")

# Criando a estrutura de dados
dados_chatbot = {
    "pergunta": pergunta_usuario,
    "resposta_automatica": "Recebi sua pergunta e estou processando a resposta."
}

# Convertendo e formatando (indent=4 deixa o visual com quebras de linha e recuos)
json_formatado = json.dumps(dados_chatbot, indent=4, ensure_ascii=False)

print("\n--- JSON Formatado ---")
print(json_formatado)