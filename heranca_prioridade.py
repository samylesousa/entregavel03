def heranca_prioridade(tarefas, recursos, teto_prioridade):

    #organizando as tarefas por prioridade 
    #a com maior prioridade é a primeira a ser executada
    ordem_execucao_inicial = sorted(tarefas, key=lambda tarefa: tarefa.prioridade, reverse=True)
    ordem_execucao_geral = []

    #definições
    prioridades_iniciais = {}
    for i in range(0, len(tarefas)):
        prioridades_iniciais[tarefas[i].nome] = tarefas[i].prioridade


    #lista para armazenar as tarefas que estão sendo executadas
    tarefas_atuais = []

    #lista para armazenar os recursos que estão sendo utilizados
    recursos_utilizados = []

    #lista para armazenar as tarefas que foram bloqueadas durante a execução
    tarefas_bloqueadas = []