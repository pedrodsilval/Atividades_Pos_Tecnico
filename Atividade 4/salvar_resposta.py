resposta = input("Digite a resposta gerada pela IA: ")

with open("respostas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(resposta + "\n")

print("Sucesso! A resposta foi salva no arquivo respostas.txt.")