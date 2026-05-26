mensagem = input("Digite a mensagem para o chatbot: ")

with open("chatbot.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(mensagem + "\n")