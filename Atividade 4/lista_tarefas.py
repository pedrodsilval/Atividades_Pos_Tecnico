print("--- Cadastro de Tarefas ---")

with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
    for i in range(1, 4):
        tarefa = input(f"Digite a {i}ª tarefa: ")
        arquivo.write(tarefa + "\n")

print("\nSucesso! As 3 tarefas foram salvas em tarefas.txt.")