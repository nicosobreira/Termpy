from lib.strings import *
import data.config as config


def menu():
    from lib.jogo import termoJogo

    opçãoUsuário = perguntaMenu()
    if opçãoUsuário == 'N':
        tutorial()
        termoJogo()
    elif opçãoUsuário == 'T':
        config.Idioma = trocarIdioma()
    elif opçãoUsuário == 'S':
        sair()


def perguntaMenu():
    OPÇÕES = ('N', 'T', 'S')

    while True:
        mostrarTexto(f'''Você deseja...
N - Nova partida["{config.Idioma}"]
T - Trocar Idioma
S - Sair''', tamanho=50)
        opção_usuário = str(input('>>> Sua opção: ')).upper()
        if opção_usuário in OPÇÕES:
            return opção_usuário


def tutorial():
    from time import sleep

    limpaTerminal()
    linha()
    print(' - ' + coloreTexto('Correto', 'Verde'))
    print(' - ' + coloreTexto('Meio Certo', 'Amarelo'))
    print(' - ' + coloreTexto('Errado', 'Vermelho'))
    linha()
    sleep(1)


def trocarIdioma():
    from lib.pastas import mostraArquivos, perguntaArquivo, diretórioAtual
    
    limpaTerminal()
    idioma_caminho = diretórioAtual() + '/data/formatado/'
    mostraArquivos(idioma_caminho)
    novo_idioma = perguntaArquivo(
        'Qual será o idioma escolhido? ', idioma_caminho)
    config.Idioma = novo_idioma
    return config.Idioma


def sair():
    from sys import exit

    limpaTerminal()
    mostrarTexto('Volte Sempre!', '-', 30)
    exit()


if __name__ == '__main__':
    while True:
        menu()
