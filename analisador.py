from lib.pastas import *
from lib.strings import limpaTerminal, mostrarTexto

ESPECIAIS = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')',
    '|', '/', '"', "'", '-', '+', '[', ']', '<', '>',
    ':', 'ª', 'º', ';', ',', '.', '?',
)


def main():
    bancoDados_caminho = bancoDadosUsuário()
    formatado_caminho = formatadoPergunta()

    # Abre o arquivo para leitura
    with open(bancoDados_caminho, 'r') as bancoDados_arquivo:
        bancoDados_LINHAS = bancoDados_arquivo.readlines()
        formatado_TERMOS = []

    # Aceita apenas palavras com 5 caracteres
    for linha in bancoDados_LINHAS:
        linha = linha.strip().upper()
        if len(linha) == 5:
            formatado_TERMOS.append(linha)

    # Procura por caracteres especiais e exclui a palavra
    for índex, palavra in enumerate(formatado_TERMOS):
        palavra = str(palavra)
        for caractere in palavra:
            for especial in ESPECIAIS:
                if caractere == especial:
                    formatado_TERMOS[índex] = palavra.replace(caractere, '')

    # Aceita apenas palavras com 5 caracteres
    for linha in formatado_TERMOS:
        if len(linha) != 5:
            formatado_TERMOS.remove(linha)

    # Apaga e abre o arquivo, se existir, senão cria um novo
    with open(formatado_caminho, 'w+') as formatado_arquivo:
        if len(formatado_TERMOS) != 0:
            for termo in formatado_TERMOS:
                formatado_arquivo.write(termo + '\n')
        else:
            formatado_arquivo.write('# Não existe NENHUM termo' + '\n')
    
    limpaTerminal()
    mostrarTexto('Analise feita com sucesso!', '~')


def bancoDadosUsuário():
    while True:
        bancoDados_caminho = diretórioAtual() + "/data/bancoDados/"
        mostraArquivos(bancoDados_caminho)
        bancoDados_arquivo = perguntaArquivo(
            'Qual é o arquivo que será escolhido? ', bancoDados_caminho)
        bancoDados_caminho += bancoDados_arquivo

        cont = continuação(bancoDados_caminho)
        if cont == True:
            print()
            return bancoDados_caminho


def formatadoPergunta():
    while True:
        formatado_caminho = diretórioAtual() + '/data/formatado/'
        formatado_arquivo = perguntaArquivo(
            'Qual será o nome do novo arquivo formatado? ', formatado_caminho, False)
        formatado_caminho += formatado_arquivo

        cont = continuação(formatado_caminho)
        if cont == True:
            return formatado_caminho




if __name__ == '__main__':
    main()
