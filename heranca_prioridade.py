def heranca_prioridade(tarefas, recursos, teto_prioridade):

    #organizando as tarefas por nome delas
    #por exemplo T1 é a primeira a executar
    ordem_execucao_inicial = sorted(tarefas, key=lambda tarefa: tarefa.nome, reverse=False)
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

    #inicializando uma variável para controlar o tempo
    tempo = 0


    #lista para armazenar os periodos
    lista_periodos = []
    for i in range(0, len(tarefas)):
        lista_periodos.append(tarefas[i].periodo)


    while(tempo<20):
        #verificando se é a primeira execução ou não
        if(tempo == 0):
            tarefas_atuais.append(ordem_execucao_inicial[0])
            recursos_utilizados.append(ordem_execucao_inicial[0].recursos)

        else:
            #verificando se tem alguma tarefa executando para diminuir o tempo dela
            if(len(tarefas_atuais)>0):
                for i in range(0, len(tarefas_atuais)-1):
                    if(tarefas_atuais[i].tempo_execucao != 0):
                        tarefas_atuais[i].tempo_execucao = tarefas_atuais[i].tempo_execucao - 1
                    else:
                        if(len(tarefas_atuais[i].recursos)>3):
                            recursos_prioridades = tarefas_atuais[i].recursos[1:-1].replace(" ", "").split(",")
                            recursos_utilizados.remove(recursos_prioridades)
                        else:
                            recursos_utilizados.remove(tarefas_atuais[i].recursos)

                        ordem_execucao_geral.append(tarefas_atuais[i].nome)
                        tarefas_atuais.pop(i)
            
            #verificando se as tarefas esperando podem ser executadas
            for elemento in ordem_execucao_inicial:
                if elemento not in tarefas_atuais:

                    #verificando se os recursos estao disponiveis
                    if(len(elemento.recursos)>3):
                        recursos_elemento = elemento.recursos[1:-1].replace(" ", "").split(",")
                        if(any(elemento in recursos_utilizados for elemento in recursos_elemento)):
                            tarefas_bloqueadas.append(elemento)
                            #atualizando a hierarquia se for necessário 
                            for i in range(0, len(tarefas_atuais)):
                                if(tarefas_atuais[i].recursos in recursos_elemento):
                                    for j in range(0, len(recursos_elemento)):
                                        if(tarefas_atuais[i].prioridade<recursos_elemento[j]):
                                            prioridades_iniciais[tarefas_atuais[i].nome] = teto_prioridade[tarefas_atuais[i].recursos]


                        else:
                            tarefas_atuais.append(elemento)
                            for i in range(0, len(recursos_elemento)):
                                if(recursos_elemento[i] not in recursos_utilizados):
                                    recursos_utilizados.append(recursos_elemento[i])

                    else:
                        if(elemento.recursos in recursos_utilizados):
                            tarefas_bloqueadas.append(elemento)
                            #atualizando a hierarquia se for necessário 
                            for i in range(0, len(tarefas_atuais)):
                                if(tarefas_atuais[i].recursos==elemento.recursos):
                                    if(tarefas_atuais[i].prioridade<elemento.prioridade):
                                        prioridades_iniciais[tarefas_atuais[i].nome] = teto_prioridade[elemento.recursos]
                        else:
                            tarefas_atuais.append(elemento)
                            recursos_utilizados.append(elemento.recursos)


            
            #verificando se alguma tarefa tem que ser executada pelo periodo
            # for i in range(0, len(lista_periodos)):
            #     if(tempo % lista_periodos[i] == 0):



        tempo = tempo + 1
    return ordem_execucao_geral