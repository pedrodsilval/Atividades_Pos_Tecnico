usuario = input("Digite o nome do usuário para registrar o acesso: ")

with open("acessos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(usuario + "\n")