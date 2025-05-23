# Cria um dicionário onde a chave é o 'id_conteudo' e o valor é uma lista com todas as interações daquele conteúdo.


# Entrada: lista de dicionários (dados do CSV).
# Saída: dicionário onde a chave é id_conteudo e o valor é uma lista de dicionários (interações).
def agrupar_por_conteudo(dados):
    agrupado = {}  # Estrutura para agrupar os conteúdos em dicionário.

    for item in dados:  # Percorre cada linha/iteração do dataset.
        id_conteudo = item['id_conteudo']  # Pega o id_conteudo para usar como chave do agrupamento.

        # Se o id_conteudo ainda não está no dicionário, cria uma nova lista para ele.
        if id_conteudo not in agrupado:
            agrupado[id_conteudo] = []  # Inicializa uma lista vazia.

        agrupado[id_conteudo].append(item)  # Adiciona a interação atual na lista correspondente.

    return agrupado  # Retorna o dicionário agrupado.
