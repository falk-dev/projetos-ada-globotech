
import csv
from typing import List, Dict, Any
from collections import defaultdict

def carregar_dados_csv(caminho: str) -> List[Dict[str, Any]]:
    dados = []
    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                dados.append(limpar_linha(linha))
            except Exception as e:
                print(f"Erro ao processar linha: {linha} | Erro: {e}")
    return dados

def limpar_linha(linha: Dict[str, str]) -> Dict[str, Any]:
    tipo_interacao = linha["tipo_interacao"].strip()
    plataforma = linha["plataforma"].strip()
    comment_text = linha["comment_text"].strip() if linha["comment_text"] else None

    try:
        id_conteudo = int(linha["id_conteudo"])
        id_usuario = int(linha["id_usuario"])
        duracao_str = linha.get("watch_duration_seconds", "").strip()
        watch_duration = int(duracao_str) if duracao_str else None
    except ValueError as e:
        raise ValueError("Erro ao converter campos numéricos.") from e

    if tipo_interacao in ["view_start"]:
        watch_duration = watch_duration if watch_duration is not None else 0
    else:
        watch_duration = watch_duration if watch_duration is not None else None

    return {
        "id_conteudo": id_conteudo,
        "nome_conteudo": linha["nome_conteudo"].strip(),
        "id_usuario": id_usuario,
        "timestamp_interacao": linha["timestamp_interacao"].strip(),
        "plataforma": plataforma,
        "tipo_interacao": tipo_interacao,
        "watch_duration_seconds": watch_duration,
        "comment_text": comment_text
    }

def agrupar_por_conteudo(dados: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    agrupado = defaultdict(lambda: {"nome_conteudo": "", "interacoes": []})
    for item in dados:
        id_conteudo = item["id_conteudo"]
        agrupado[id_conteudo]["nome_conteudo"] = item["nome_conteudo"]
        agrupado[id_conteudo]["interacoes"].append(item)
    return agrupado

def calcular_total_interacoes_por_conteudo(dados: Dict[int, Dict[str, Any]]) -> Dict[int, int]:
    resultado = {}
    for id_conteudo, info in dados.items():
        total = sum(1 for i in info["interacoes"] if i["tipo_interacao"] in ["like", "share", "comment"])
        resultado[id_conteudo] = total
    return resultado

def contar_tipo_interacao_por_conteudo(dados: Dict[int, Dict[str, Any]]) -> Dict[int, Dict[str, int]]:
    resultado = {}
    for id_conteudo, info in dados.items():
        contagem = {}
        for i in info["interacoes"]:
            tipo = i["tipo_interacao"]
            contagem[tipo] = contagem.get(tipo, 0) + 1
        resultado[id_conteudo] = contagem
    return resultado

def tempo_total_visualizacao_por_conteudo(dados: Dict[int, Dict[str, Any]]) -> Dict[int, int]:
    resultado = {}
    for id_conteudo, info in dados.items():
        total = sum(i["watch_duration_seconds"] or 0 for i in info["interacoes"])
        resultado[id_conteudo] = total
    return resultado

def media_tempo_visualizacao_por_conteudo(dados: Dict[int, Dict[str, Any]]) -> Dict[int, float]:
    resultado = {}
    for id_conteudo, info in dados.items():
        duracoes = [i["watch_duration_seconds"] for i in info["interacoes"] if i["watch_duration_seconds"]]
        media = sum(duracoes) / len(duracoes) if duracoes else 0.0
        resultado[id_conteudo] = round(media, 2)
    return resultado

def listar_comentarios_por_conteudo(id_conteudo: int, dados: Dict[int, Dict[str, Any]]) -> List[str]:
    if id_conteudo not in dados:
        return []
    return [i["comment_text"] for i in dados[id_conteudo]["interacoes"] if i["tipo_interacao"] == "comment" and i["comment_text"]]

def top_5_conteudos_por_visualizacao(dados: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
    totais = tempo_total_visualizacao_por_conteudo(dados)
    ordenados = sorted(totais.items(), key=lambda x: x[1], reverse=True)[:5]
    return [{"id_conteudo": k, "nome": dados[k]["nome_conteudo"], "tempo_total": v} for k, v in ordenados]
