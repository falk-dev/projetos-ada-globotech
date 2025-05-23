# Função responsável por ler um arquivo CSV e transformar em uma lista de dicionários.

import csv  # Importação do módulo nativo csv para manipular arquivos CSV.

# Entrada: caminho do arquivo CSV.
# Saída: uma lista de dicionários, onde cada dicionário representa uma linha do CSV.
def carregar_csv(caminho_arquivo):
    dados = []  # 🔸 Lista → Estrutura de dados usada para armazenar cada linha do CSV como um dicionário.

    # 🔸 Abre o arquivo e garante que ele será fechado automaticamente após uso com o 'with'.
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # 🔸 csv.DictReader → Lê cada linha do CSV e transforma em um dicionário.

        # Percorre cada linha do arquivo CSV com 'for'.
        for linha in leitor:
            dados.append(linha)  # Adiciona cada dicionário na lista de dados com '.append()'.

    return dados  # Retorna uma lista de dicionários com os dados lidos.
