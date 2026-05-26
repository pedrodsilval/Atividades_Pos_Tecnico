# Solicita um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o resto da divisão por 2 é zero
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")