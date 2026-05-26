# Solicita uma pergunta ao usuário [cite: 391]
pergunta = input("Digite uma pergunta para a IA: ")

# Salva a pergunta em um arquivo chamado historico_ia.txt [cite: 392]
with open("historico_ia.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Usuário: {pergunta}\n")

# Exibe uma mensagem de confirmação [cite: 393]
print("Sucesso! Sua pergunta foi salva no histórico de atendimento.")