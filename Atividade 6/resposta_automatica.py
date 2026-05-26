# Solicita uma pergunta ao usuário [cite: 361]
pergunta = input("Faça uma pergunta: ").strip().lower()

# Estrutura condicional simulando uma IA 
if "clima" in pergunta:
    resposta = "O clima hoje parece ótimo para programar!"
elif "python" in pergunta:
    resposta = "Python é uma linguagem fantástica para Inteligência Artificial."
else:
    resposta = "Ainda estou aprendendo e não tenho a resposta para isso."

# Exibe a resposta na tela 
print(f"Assistente: {resposta}")