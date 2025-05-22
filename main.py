
from processamento import (
    carregar_dados_csv,
    agrupar_por_conteudo,
    calcular_total_interacoes_por_conteudo,
    contar_tipo_interacao_por_conteudo,
    tempo_total_visualizacao_por_conteudo,
    media_tempo_visualizacao_por_conteudo,
    listar_comentarios_por_conteudo,
    top_5_conteudos_por_visualizacao
)

CAMINHO_ARQUIVO = "interacoes_globo.csv"

def main():
    print("Carregando e limpando dados...")
    dados_limpos = carregar_dados_csv(CAMINHO_ARQUIVO)

    print("Estruturando dados por conteúdo...")
    dados_estruturados = agrupar_por_conteudo(dados_limpos)

    print("\n Total de interações por conteúdo:")
    total_interacoes = calcular_total_interacoes_por_conteudo(dados_estruturados)
    for id_c, total in total_interacoes.items():
        print(f"ID {id_c} - Total: {total}")

    print("\n Contagem por tipo de interação:")
    tipos = contar_tipo_interacao_por_conteudo(dados_estruturados)
    for id_c, detalhes in tipos.items():
        print(f"ID {id_c} - {detalhes}")

    print("\n Tempo total de visualização por conteúdo:")
    tempo_total = tempo_total_visualizacao_por_conteudo(dados_estruturados)
    for id_c, tempo in tempo_total.items():
        print(f"ID {id_c} - {tempo} segundos")

    print("\n Média de tempo de visualização:")
    medias = media_tempo_visualizacao_por_conteudo(dados_estruturados)
    for id_c, media in medias.items():
        print(f"ID {id_c} - Média: {media} segundos")

    print("\n Comentários do conteúdo 3:")
    comentarios = listar_comentarios_por_conteudo(3, dados_estruturados)
    for c in comentarios:
        print(f"- {c}")

    print("\n Top 5 conteúdos com mais tempo assistido:")
    top5 = top_5_conteudos_por_visualizacao(dados_estruturados)
    for item in top5:
        print(f"ID {item['id_conteudo']} - {item['nome']} - {item['tempo_total']} segundos")

if __name__ == "__main__":
    main()
