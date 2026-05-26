# Solicita uma pergunta [cite: 399]
mensagem = input("Você: ").strip().lower()

# Responde automaticamente [cite: 400]
if mensagem == "oi":
    print("Bot: Olá!") # [cite: 401]
elif mensagem == "como você funciona?":
    print("Bot: Utilizo programação e IA.") # [cite: 402]
else:
    print("Bot: Não compreendi.") # [cite: 403]