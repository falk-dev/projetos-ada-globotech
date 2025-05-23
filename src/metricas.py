# Arquivo responsável por calcular todas as métricas do projeto, incluindo:
# - Total de interações e contagem por tipo de Interação do conteúdo
# - Tempo total e média do tempo de visualização
# - Listagem de comentários
# - Top 5 conteúdos com mais tempo de visualização


# Calcula total de interações por tipo (like, share, comment, view_start) para cada conteúdo.
def calcular_interacoes(dados):
    metricas = {}  # Dicionário - Chave: id_conteudo, Valor: outro dicionário com contagens.

    for item in dados:  # Percorre cada linha/iteração do dataset.
        id_conteudo = item['id_conteudo']
        nome_conteudo = item['nome_conteudo']
        tipo = item['tipo_interacao']  # Tipo de interação: like, share, comment, view_start...

        # Se o conteúdo ainda não foi registrado nas métricas, inicializa as contagens.
        if id_conteudo not in metricas:
            metricas[id_conteudo] = {
                'nome_conteudo': nome_conteudo,
                'like': 0,
                'share': 0,
                'comment': 0,
                'view_start': 0,
                'total': 0
            }

        # Incrementa a contagem do tipo de interação, se existir na estrutura.
        if tipo in metricas[id_conteudo]:
            metricas[id_conteudo][tipo] += 1
        else:
            metricas[id_conteudo][tipo] = 1  #Caso apareça algum tipo novo, adiciona dinamicamente.

        metricas[id_conteudo]['total'] += 1  #Incrementa o total de interações.

    return metricas # Retorna o dicionário com as métricas calculadas.


# Calcula o tempo total e a média de tempo de visualização para cada conteúdo.
def calcular_tempo_visualizacao(dados):
    resultado = {}  # Dicionário - Chave: id_conteudo, Valor: tempo total e média.

    for item in dados:  # Percorre cada linha do dataset.
        id_conteudo = item['id_conteudo']
        nome = item['nome_conteudo']
        duracao = item.get('watch_duration_seconds', 0)  # Tempo de visualização.

        # Se ainda não há dados para esse conteúdo, inicializa.
        if id_conteudo not in resultado:
            resultado[id_conteudo] = {
                'nome_conteudo': nome,
                'total_duracao': 0,
                'contagem_visualizacoes': 0
            }

        # Se há tempo registrado (positivo), acumula.
        if isinstance(duracao, int) and duracao > 0:
            resultado[id_conteudo]['total_duracao'] += duracao
            resultado[id_conteudo]['contagem_visualizacoes'] += 1

    # Calcula a média de duração.
    for id_conteudo, info in resultado.items():
        if info['contagem_visualizacoes'] > 0:
            info['media_duracao'] = info['total_duracao'] / info['contagem_visualizacoes']
        else:
            info['media_duracao'] = 0

    return resultado # Retorna o dicionário com as métricas de tempo de visualização.


# Gera um dicionário agrupando os comentários por conteúdo.
def listar_comentarios_por_conteudo(dados):
    comentarios_agrupados = {}  # Dicionário - Chave: id_conteudo, Valor: lista de comentários.

    for item in dados:  # Percorre cada linha do dataset.
        if item['tipo_interacao'] == 'comment':  # Considera apenas interações do tipo comentário.
            id_conteudo = item['id_conteudo']
            nome_conteudo = item['nome_conteudo']
            comentario = item.get('comment_text', '').strip()  # Obtém o texto do comentário.

            if comentario:  # Se não estiver vazio, processa.
                if id_conteudo not in comentarios_agrupados:
                    comentarios_agrupados[id_conteudo] = {
                        'nome_conteudo': nome_conteudo,
                        'comentarios': []
                    }

                comentarios_agrupados[id_conteudo]['comentarios'].append(comentario)

    return comentarios_agrupados # Retorna o dicionário com os comentários agrupados por conteúdo.


# Retorna os 5 conteúdos com maior tempo total de visualização.
def top_5_conteudos_mais_visualizados(tempo_metricas):
    #  Ordena com o 'sorted()' os conteúdos pelo tempo total de visualização, em ordem decrescente.
    ordenado = sorted(tempo_metricas.items(), key=lambda x: x[1]['total_duracao'], reverse=True)
    return ordenado[:5]  # Retorna apenas os 5 primeiros.
