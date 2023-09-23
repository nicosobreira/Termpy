from lib.jogo import *
from lib.strings import *


def termoJogo():
    partida = 1
    jogo_lista = []
    termo_gerador = geradorTermo()
    while True:
        exibePartida('termo', jogo_lista)
        usr_termo_input = perguntaTermo('')
        jogo_lista.append(jogoResultadoLista(usr_termo_input, termo_gerador))
        if usr_termo_input == termo_gerador:
            exibePartida(jogo_lista)
            mostrar(f'Acertou na {partida}ª jogada :)', '~')
            break
        elif partida == 6:
            exibePartida('termo', jogo_lista)
            mostrar(f'A palavra era {termo_gerador} :(', '~')
            break
        partida += 1
