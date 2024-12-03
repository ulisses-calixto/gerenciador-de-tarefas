class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = {}

    def adicionar_tarefa(self, nome_tarefa):
        self.tarefas[nome_tarefa] = 'Pendente'
        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso.")

    def marcar_como_concluida(self, nome_tarefa):
        if nome_tarefa in self.tarefas:
            self.tarefas[nome_tarefa] = 'Concluída'
            print(f"Tarefa '{nome_tarefa}' Marcada como concluída.")
        else:
            print(f"Tarefa '{nome_tarefa}' não encontrada.")

    def remover_tarefa(self, nome_tarefa):
        if nome_tarefa in self.tarefas:
            del self.tarefas[nome_tarefa]
            print(f"Tarefa '{nome_tarefa}' removida.")
        else:
            print(f"Tarefa '{nome_tarefa}' não encontrada.")

    def listar_tarefas(self):
        print("\nLista de Tarefas:")
        for tarefa, estado in self.tarefas.items():
            print(f"{tarefa} - {estado}")

    def pesquisar_tarefa(self, nome_tarefa):
        if nome_tarefa in self.tarefas:
            print(f"Tarefa encontrada: {nome_tarefa} - {self.tarefas[nome_tarefa]}")
        else:
            print(f"Tarefa '{nome_tarefa}' não encontrada.")

geren = GerenciadorDeTarefas()
geren.adicionar_tarefa("Estudar POO")
geren.adicionar_tarefa("Fazer compras")
geren.marcar_como_concluida("Estudar POO")
geren.listar_tarefas()
