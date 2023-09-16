from lib.strings import cores, continuação


def diretórioAtual():
    import os

    diretório_atual = os.getcwd()
    return str(diretório_atual)


def bancoDadosUsuário():
    while True:
        bancoDados_caminho = diretórioAtual() + "/dados/bancoDados/"
        bancoDados_arquivo = str(input('Qual é o arquivo da Base de Dados? '))
        bancoDados_caminho += bancoDados_arquivo

        cont = continuação(bancoDados_caminho)
        if cont == True:
            print()
            return bancoDados_caminho


def formatadoPergunta():
    while True:
        formatado_caminho = diretórioAtual() + '/dados/formatado/'
        formatado_arquivo = str(input('Qual é o nome do arquivo final? '))
        formatado_caminho += formatado_arquivo

        print(cores('Todos os arquivos serão excluídos', 'Vermelho'))
        cont = continuação(formatado_caminho)
        if cont == True:
            with open(formatado_caminho, 'w') as formatado:
                formatado.write(
                    '# Arquivo criado/editado usando o analisador\n\n')
            print()
            return formatado_caminho
