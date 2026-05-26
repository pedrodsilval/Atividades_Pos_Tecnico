# Pede o número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)

# O range(1, 11) vai gerar os números de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")