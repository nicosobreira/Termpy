from lib.strings import coloreTexto, errorMensagem


def mostraArquivos(caminho):
    from os import listdir
    from lib.strings import mostraLista

    diretório = listdir(caminho)
    if diretório[0][:2] == '__':
        diretório.pop(0)
    mostraLista(diretório)


def diretórioAtual():
    from os import getcwd

    diretório_atual = getcwd()
    return str(diretório_atual)


def continuação(caminho):
    while True:
        print('Esse é o caminho: ' + coloreTexto(caminho, 'Amarelo'))
        continuação = str(input('Deseja continuar? [S/N] '))
        if continuação in 'Ss':
            return True
        else:
            return False


def perguntaArquivo(mensagem, caminho, verificação=True):
    from os import listdir

    while True:
        arquivo = str(input('>>> ' + mensagem))
        if verificação:
            if arquivo not in listdir(caminho):
                errorMensagem('Digite um nome de arquivo válido')
            else:
                return arquivo
        else:
            return arquivo
