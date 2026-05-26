print("--- Assistente Iniciado (Digite 'sair' para encerrar) ---")

# Continue solicitando perguntas ao usuário [cite: 408]
while True:
    pergunta = input("Como posso ajudar? ").strip().lower()
    
    # Encerre apenas quando o usuário digitar a palavra "sair" [cite: 409]
    if pergunta == "sair":
        print("Encerrando o sistema...")
        break
        
    print(f"Processando a pergunta: '{pergunta}'...")www