print("--- Chatbot de Atendimento Iniciado ---")

# Loop infinito para interação contínua
while True:
    mensagem = input("Você: ").strip().lower()
    
    # Respostas programadas
    if mensagem == "oi":
        print("Chatbot: Olá! Como posso ajudar?")
    elif mensagem == "tchau":
        print("Chatbot: Encerrando o atendimento. Até logo!")
        break # Quebra o loop e encerra o programa
    else:
        print("Chatbot: Não entendi sua mensagem.")