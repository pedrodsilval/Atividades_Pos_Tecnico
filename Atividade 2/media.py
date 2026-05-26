# Solicita os três números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Calcula a média (os parênteses garantem que a soma ocorra antes da divisão)
media = (n1 + n2 + n3) / 3

# Exibe o resultado formatado com 2 casas decimais
print(f"A média aritmética é: {media:.2f}")