# Arquivo responsável por salvar os dados processados em arquivos CSV na pasta outputs.

import csv  # Módulo nativo do Python usado para manipulação de arquivos CSV.



# Salva o total de interações por conteúdo em um arquivo CSV.
def salvar_metricas_interacoes(caminho, metricas):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)  # Cria um objeto para escrever no CSV.

        # Cabeçalho do arquivo CSV.
        escritor.writerow(['id_conteudo', 'nome_conteudo', 'like', 'share', 'comment', 'view_start', 'total'])

        # Loop sobre as métricas para escrever cada linha.
        for id_conteudo, info in metricas.items():
            escritor.writerow([
                id_conteudo,
                info['nome_conteudo'],
                info['like'],
                info['share'],
                info['comment'],
                info['view_start'],
                info['total']
            ])


# Salva tempo total e média de visualização por conteúdo em um arquivo CSV.
def salvar_tempo_visualizacao(caminho, metricas):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        # Cabeçalho do CSV.
        escritor.writerow(['id_conteudo', 'nome_conteudo', 'total_duracao', 'media_duracao'])
        
        # Loop para escrever os dados de tempo de visualização.
        for id_conteudo, info in metricas.items():
            escritor.writerow([
                id_conteudo,
                info['nome_conteudo'],
                info['total_duracao'],
                round(info['media_duracao'], 2)  # Arredonda a média para 2 casas decimais.
            ])


# Salva o top 5 conteúdos com mais tempo de visualização em um arquivo CSV.
def salvar_top5(caminho, top5):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        # Cabeçalho do CSV.
        escritor.writerow(['rank', 'id_conteudo', 'nome_conteudo', 'total_duracao'])

        # Loop para escrever os dados do top 5.
        for rank, (id_conteudo, info) in enumerate(top5, 1):  # Cria contador automático a partir de 1 com 'enumerate'.
            escritor.writerow([
                rank,
                id_conteudo,
                info['nome_conteudo'],
                info['total_duracao']
            ])


# Salva todos os comentários agrupados por conteúdo em um CSV.
def salvar_comentarios(caminho, comentarios_agrupados):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        # Cabeçalho do CSV.
        escritor.writerow(['id_conteudo', 'nome_conteudo', 'comentario'])

        # Loop para escrever os comentários agrupados.
        for id_conteudo, info in comentarios_agrupados.items():
            for comentario in info['comentarios']:
                escritor.writerow([id_conteudo, info['nome_conteudo'], comentario]) 
                
