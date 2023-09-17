from lib.strings import *
from lib.jogo import *


def tutorial():
    from time import sleep

    linha_str = linha('-')
    print(linha_str)
    print(' - ' + cores('Correto', 'Verde'))
    print(' - ' + cores('Meio Certo', 'Amarelo'))
    print(' - ' + cores('Errado', 'Vermelho'))
    print(linha_str)
    sleep(1)


def novoJogo(idioma_usuário):
    tutorial()
    partida = 0

    partida += 1
    contador = 1
    termo_lista = []
    termo_palavra = geradorTermo(idioma_usuário)
    while True:
        exibePartida(termo_lista, partida)
        usr_input_palavra = perguntaTermo('')
        jogada = jogoResultado(usr_input_palavra, termo_palavra)
        termo_lista.append(jogada)
        if usr_input_palavra == termo_palavra or contador == 6:
            break
        contador += 1
    exibePartida(termo_lista, partida)

    if contador == 6:
        mostrar(f'A palavra era {termo_palavra} :(', '~')
    else:
        mostrar(f'{contador}º jogada :)', '~')


def novoIdioma():
    idioma_usuário = escolhaIdioma()
    idioma_usuário = f'{idioma_usuário}_termos.py'


def sair():
    limpaTerminal()
    mostrar('Volte Sempre!', '-', 30)
