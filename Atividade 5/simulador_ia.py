import json

# Criando um dicionário Python padrão
resposta_ia = {
    "pergunta": "O que é Python?",
    "resposta": "Python é uma linguagem de programação de alto nível e de propósito geral."
}

# Convertendo o dicionário para uma string no formato JSON
# ensure_ascii=False garante que os acentos não fiquem distorcidos
json_dados = json.dumps(resposta_ia, indent=4, ensure_ascii=False)

print("Dados convertidos para o formato JSON:")
print(json_dados)