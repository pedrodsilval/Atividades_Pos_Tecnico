# Credenciais corretas cadastradas no "banco de dados"
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

# Solicita os dados ao usuário
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")

# Verifica se os dados batem
if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
    print("Acesso permitido")
else:
    print("Acesso negado")