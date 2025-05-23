# Arquivo que executa o programa inteiro, oferece um menu interativo no console
# e permite calcular e visualizar todas as métricas, além de gerar arquivos CSV.

# Importações dos módulos internos (criados dentro da pasta /src) e do módulo nativo 'os'.
import os

from src.leitura import carregar_csv  # Leitura do arquivo CSV
from src.limpeza import limpar_espacos, tratar_dados_numericos  # Limpeza de dados
from src.metricas import (  # Cálculo das métricas
    calcular_interacoes,
    calcular_tempo_visualizacao,
    listar_comentarios_por_conteudo,
    top_5_conteudos_mais_visualizados
)
from src.salvar import (  # Salvamento dos resultados em CSV
    salvar_metricas_interacoes,
    salvar_tempo_visualizacao,
    salvar_top5,
    salvar_comentarios
)


# Converte segundos para horas e minutos.
def formatar_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas}h {minutos}m"


# Exibir total de interações no terminal
def exibir_metricas_interacoes(metricas):
    # Exibe o total de interações e os tipos delas (likes, shares, comments, views) para cada conteúdo.
    print("\n\n|| TOTAL DE INTERAÇÕES E SEUS TIPOS POR CONTEÚDO:")
    for id_conteudo, info in metricas.items():
        print(f"\nID {id_conteudo}: {info['nome_conteudo']}")
        print(f" Likes: {info['like']} | Shares: {info['share']} | Comments: {info['comment']} | Views: {info['view_start']}")
        print(f" Total de Interações: {info['total']}")


# Exibir tempo de visualização no terminal
def exibir_metricas_tempo(metricas): 
    # Exibe o tempo total e a média de visualização para cada conteúdo.
    print("\n\n|| TEMPO TOTAL E MÉDIA DE VISUALIZAÇÃO POR CONTEÚDO:")
    for id_conteudo, info in metricas.items():
        total = info['total_duracao']
        media = info['media_duracao']
        print(f"\nID {id_conteudo}: {info['nome_conteudo']}")
        print(f" Tempo Total: {formatar_tempo(total)}")
        print(f" Média de Visualização: {formatar_tempo(int(media))}")


# Exibir top 5 conteúdos com mais tempo de visualização
def exibir_top_5(top5):
    print("\n\n|| TOP 5 CONTEÚDOS MAIS VISUALIZADOS:")
    for rank, (id_conteudo, info) in enumerate(top5, 1): # Cria contador automático a partir de 1 com 'enumerate'.
        # Imprime o rank, id_conteudo e nome do conteúdo.
        print(f" {rank}- ID {id_conteudo}: {info['nome_conteudo']}")
        print(f"Tempo Total: {formatar_tempo(info['total_duracao'])}")


# Exibir todos os comentários agrupados por conteúdo
def exibir_todos_comentarios(comentarios_agrupados):
    print("\n\n|| COMENTÁRIOS AGRUPADOS POR CONTEÚDO:")
    # Verifica se há comentários agrupados
    if comentarios_agrupados:
        for id_conteudo, info in comentarios_agrupados.items(): # Verifica se há comentários
            # Se houver, imprime o id_conteudo e o nome do conteúdo
            # e depois imprime todos os comentários associados a esse conteúdo.
            print(f"\nID {id_conteudo}: {info['nome_conteudo']}")
            for comentario in info['comentarios']:
                # Se o comentário não for vazio, imprime o comentário.
                print(f" - {comentario}")
    # Se não houver comentários, imprime uma mensagem informando que não há comentários.
    else:
        print("\nNão há comentários registrados nos dados.")


# Função para apagar arquivos na pasta outputs
def limpar_outputs():
    pasta = 'outputs'
    # Verifica se a pasta existe
    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        # Verifica se o caminho é um arquivo e tenta removê-lo
        try:
            if os.path.isfile(caminho):
                os.remove(caminho)
                print(f"Arquivo {caminho} deletado com sucesso.")
        # Se não for possível deletar, imprime o erro
        except Exception as e:
            print(f"Erro ao deletar {caminho}: {e}")


# Pergunta se o usuário quer voltar ao menu ou sair
def voltar_ou_sair():
    while True: # Loop para garantir que o usuário escolha uma opção válida
        escolha = input("\n\nDeseja voltar ao menu ou sair?\n1 - Voltar ao Menu\n2 - Apenas Sair\n3 - Sair e Limpar Outputs\nEscolha: ")
        # Se o usuário escolher 1, retorna True para voltar ao menu
        if escolha == '1':
            return True
        # Se o usuário escolher 2, apenas sai do programa
        elif escolha == '2':
            print("\nSaindo...")
            exit()
            # Se o usuário escolher 3, limpa os arquivos de saída e sai do programa
        elif escolha == '3':
            limpar_outputs()
            print("\nArquivos de saída apagados. Saindo...")
            exit()
        # Se o usuário não escolher uma opção válida, imprime uma mensagem de erro
        else:
            print("Opção inválida. Digite 1 ou 2.")


# Função principal do programa
def main():
    # Caminhos dos arquivos de entrada e saída
    caminho_entrada = 'data/interacoes_globo.csv'
    caminho_saida_interacoes = 'outputs/metricas_interacoes.csv'
    caminho_saida_tempo = 'outputs/metricas_tempo.csv'
    caminho_saida_top5 = 'outputs/top5_conteudos.csv'
    caminho_saida_comentarios = 'outputs/comentarios_por_conteudo.csv'

    # Pipeline de processamento:
    dados = carregar_csv(caminho_entrada)
    dados = limpar_espacos(dados)
    dados = tratar_dados_numericos(dados)

    # Cálculo das métricas
    metricas_interacoes = calcular_interacoes(dados)
    metricas_tempo = calcular_tempo_visualizacao(dados)
    comentarios_agrupados = listar_comentarios_por_conteudo(dados)
    top5 = top_5_conteudos_mais_visualizados(metricas_tempo)

    # Salva interações e tempo automaticamente
    salvar_metricas_interacoes(caminho_saida_interacoes, metricas_interacoes)
    salvar_tempo_visualizacao(caminho_saida_tempo, metricas_tempo)

    # Loop do menu
    while True: 
        print("\n|| MENU:")
        print("1 - Ver Total de Interações")
        print("2 - Ver Tempo de Visualização")
        print("3 - Ver Top 5 Conteúdos Mais Visualizados")
        print("4 - Listar Comentários por Conteúdo")
        print("5 - Ver Todas as Métricas no Terminal")
        print("6 - Gerar Todos os CSVs")
        print("7 - Sair (limpar outputs)")

        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida pelo usuário
        # e chama a função correspondente.
        if opcao == '1':
            exibir_metricas_interacoes(metricas_interacoes)
            voltar_ou_sair()

        elif opcao == '2':
            exibir_metricas_tempo(metricas_tempo)
            voltar_ou_sair()

        elif opcao == '3':
            exibir_top_5(top5)
            voltar_ou_sair()

        elif opcao == '4':
            exibir_todos_comentarios(comentarios_agrupados)
            voltar_ou_sair()

        elif opcao == '5':
            exibir_metricas_interacoes(metricas_interacoes)
            exibir_metricas_tempo(metricas_tempo)
            exibir_top_5(top5)
            exibir_todos_comentarios(comentarios_agrupados)
            voltar_ou_sair()

        elif opcao == '6':
            salvar_metricas_interacoes(caminho_saida_interacoes, metricas_interacoes)
            salvar_tempo_visualizacao(caminho_saida_tempo, metricas_tempo)
            salvar_top5(caminho_saida_top5, top5)
            salvar_comentarios(caminho_saida_comentarios, comentarios_agrupados)
            print("\nTodos os arquivos CSV foram gerados na pasta 'outputs'.")
            voltar_ou_sair()

        elif opcao == '7':
            limpar_outputs()
            print("\nArquivos de saída apagados. Saindo...")
            break

        # Se o usuário não escolher uma opção válida, imprime uma mensagem de erro.
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada do programa - Se este arquivo for executado diretamente, roda a função main().
if __name__ == '__main__':
    main()
