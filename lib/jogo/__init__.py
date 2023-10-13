from lib.strings import *


def termoJogo():
    partida = 1
    jogo_lista = []
    termo_gerador = geradorTermo()
    while True:
        exibePartida(jogo_lista)
        usr_termo_input = perguntaTermo('')
        jogo_lista.append(jogoResultadoLista(usr_termo_input, termo_gerador))
        if usr_termo_input == termo_gerador:
            exibePartida(jogo_lista)
            mostrarTexto(f'Acertou na {partida}ª jogada :)', '~')
            break
        elif partida == 6:
            exibePartida(jogo_lista)
            mostrarTexto(f'A palavra era {termo_gerador} :(', '~')
            break
        partida += 1


def geradorTermo():
    from data.config import Idioma
    from random import choice
    from lib.pastas import diretórioAtual

    termo_caminho = diretórioAtual() + '/data/formatado/' + Idioma
    with open(termo_caminho, 'r') as termos_arquivo:
        TERMOS = termos_arquivo.readlines()

    return choice(TERMOS)


def perguntaTermo(texto=''):
    while True:
        usr_termo = str(input(texto)).upper()
        if len(usr_termo) != 5:
            errorMensagem('5 dígitos apenas')
        else:
            return usr_termo


def jogoResultadoLista(usr_termo, termo_geradorTermo):
    usr_termo_list = []

    for índex, letra in enumerate(usr_termo):
        if letra in termo_geradorTermo:
            if índex == termo_geradorTermo.find(letra):
                letra_cor = coloreTexto(letra, 'Verde')
            else:
                letra_cor = coloreTexto(letra, 'Amarelo')
        else:
            letra_cor = coloreTexto(letra, 'Vermelho')
        print(letra_cor, end='')
        usr_termo_list.append(letra_cor)
    print()
    usr_termo_str = ' '.join(usr_termo_list)
    return usr_termo_str


def exibePartida(jogo_lista):
    from lib.strings import limpaTerminal, mostrarTexto

    limpaTerminal()
    mostrarTexto(f' -- Termpy --', '~')
    mostraLista(jogo_lista)
