class Tarefas:
    def __init__(self, tarefa, tempo_execucao, tempo_bloqueio, periodo, recursos, prioridade):
        self.nome = tarefa
        self.tempo_execucao = tempo_execucao
        self.tempo_bloqueio = tempo_bloqueio
        self.periodo = periodo
        self.tempo_restante = tempo_execucao
        self.bloqueado = False
        self.recursos = recursos
        self.prioridade = prioridade
        self.prioridade_atual = prioridade

    def __repr__(self):
        return f"Tarefas(nome={self.nome})"


class Recursos:
    def __init__(self, recurso, teto):
        self.recurso = recurso
        self.teto = teto
        self.tarefa = None
    
    def __repr__(self):
        return f"Recursos(nome={self.recurso}, valor={self.teto})"