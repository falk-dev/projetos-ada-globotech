# Arquivo responsável pela limpeza dos dados:
# - Remoção de espaços desnecessários nas strings.
# - Conversão de valores numéricos (como id_conteudo e watch_duration_seconds) para inteiros.
# - Tratamento de valores inválidos (como strings vazias ou não numéricas) para zero.
# - Conversão de valores de data para o formato correto.


# Função para remover espaços em branco no início e no fim dos valores das colunas.
def limpar_espacos(dados):
    # Laço externo percorre cada item (linha) da lista de dicionários.
    for item in dados:
        # Laço interno percorre cada chave do dicionário.
        for chave in item:
            # Verifica se o valor da chave é uma string (str) usando isinstance.
            if isinstance(item[chave], str):
                #  Remove espaços em branco antes e depois da string com o método '.strip()'.
                item[chave] = item[chave].strip()

    return dados  # Retorna a lista de dicionários já tratada.


# Função para converter as colunas 'id_conteudo' e 'watch_duration_seconds' de string para inteiro.
def tratar_dados_numericos(dados):
    for item in dados:  # Percorre cada linha (dicionário) da lista.
        # Conversão do campo 'id_conteudo' para inteiro.
        try:
            item['id_conteudo'] = int(item.get('id_conteudo', 0))
        except ValueError:
            item['id_conteudo'] = 0  # Se falhar na conversão, atribui 0.

        # Processamento do campo 'watch_duration_seconds'.
        valor = item.get('watch_duration_seconds', '').strip()  # Obtém o valor e remove espaços.

        try:
            # Verifica se o valor é composto apenas por dígitos e converte para inteiro.
            item['watch_duration_seconds'] = int(valor) if valor.isdigit() else 0
        except ValueError:
            item['watch_duration_seconds'] = 0  # Se falhar, atribui 0.

    return dados  # Retorna a lista de dicionários com os campos tratados.
