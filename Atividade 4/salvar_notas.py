nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nota 1: {nota1}\n")
    arquivo.write(f"Nota 2: {nota2}\n")