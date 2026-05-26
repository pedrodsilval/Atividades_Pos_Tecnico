# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica o desempenho com base na nota
if nota >= 9.0:
    print("Desempenho excelente!")
elif nota >= 7.0:
    print("Desempenho bom!")
elif nota >= 5.0:
    print("Desempenho razoável!")
else:
    print("Desempenho insuficiente!")