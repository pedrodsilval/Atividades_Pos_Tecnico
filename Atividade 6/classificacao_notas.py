# Solicita 3 notas [cite: 415]
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

# Calcula a média [cite: 416]
media = (n1 + n2 + n3) / 3

# Exibe o resultado baseado no desempenho [cite: 417]
if media >= 9.0:
    print("Excelente desempenho") # [cite: 421]
elif media >= 7.0:
    print("Bom desempenho") # [cite: 422]
else:
    print("Desempenho insuficiente") # [cite: 423]