
from processamento import (
    carregar_dados_csv,
    agrupar_por_conteudo,
    calcular_total_interacoes_por_conteudo,
    contar_tipo_interacao_por_conteudo,
    tempo_total_visualizacao_por_conteudo,
    media_tempo_visualizacao_por_conteudo,
    top_5_conteudos_por_visualizacao
)
import json

def salvar_relatorio(resultados: dict, nome_arquivo: str = "relatorio_resultados.json"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=4)
        print(f"Relatório salvo com sucesso em: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar relatório: {e}")

def rodar_pipeline(caminho_csv: str):
    resultados = {}

    try:
        print("1. Carregando dados...")
        dados = carregar_dados_csv(caminho_csv)
        resultados["quantidade_total_interacoes"] = len(dados)
    except Exception as e:
        print("Erro ao carregar dados:", e)
        return

    try:
        print("2. Estruturando por conteúdo...")
        dados_estruturados = agrupar_por_conteudo(dados)
    except Exception as e:
        print("Erro ao estruturar dados:", e)
        return

    try:
        print("3. Calculando métricas...")
        resultados["total_interacoes"] = calcular_total_interacoes_por_conteudo(dados_estruturados)
        resultados["contagem_por_tipo"] = contar_tipo_interacao_por_conteudo(dados_estruturados)
        resultados["tempo_total_visualizacao"] = tempo_total_visualizacao_por_conteudo(dados_estruturados)
        resultados["media_tempo_visualizacao"] = media_tempo_visualizacao_por_conteudo(dados_estruturados)
        resultados["top5_visualizacao"] = top_5_conteudos_por_visualizacao(dados_estruturados)
    except Exception as e:
        print("Erro ao calcular métricas:", e)
        return

    try:
        print("4. Salvando relatório...")
        salvar_relatorio(resultados)
    except Exception as e:
        print("Erro ao exportar relatório:", e)

    print("\nPipeline executada com sucesso.")
    return resultados

if __name__ == "__main__":
    rodar_pipeline("interacoes_globo.csv")
