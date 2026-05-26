# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica o sinal do número
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")