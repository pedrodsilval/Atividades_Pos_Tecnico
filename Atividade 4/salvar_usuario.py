nome = input("Digite o nome do usuário: ")

with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(nome + "\n")