soma_notas = 0

# Loop para receber as 5 notas
for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota do aluno: "))
    soma_notas += nota

# Calcula a média
media = soma_notas / 5
print(f"\nA média final do aluno é: {media:.2f}")

# Classifica o aluno (considerando média 7.0 para aprovação)
if media >= 7.0:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")