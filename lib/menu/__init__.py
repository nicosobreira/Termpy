from lib.strings import *
from lib.jogo import *


def tutorial():
    from time import sleep

    limpaTerminal()
    linha_str = linha('-')
    print(linha_str)
    print(' - ' + cores('Correto', 'Verde'))
    print(' - ' + cores('Meio Certo', 'Amarelo'))
    print(' - ' + cores('Errado', 'Vermelho'))
    print(linha_str)
    sleep(1)


def novoJogo(idioma_usuário):
    tutorial()

    contador = 1
    termo_lista = []
    termo_palavra = geradorTermo(idioma_usuário)
    print(idioma_usuário)
    while True:
        exibePartida(termo_lista)
        usr_input_palavra = perguntaTermo('')
        jogada = jogoResultado(usr_input_palavra, termo_palavra)
        termo_lista.append(jogada)
        if usr_input_palavra == termo_palavra or contador == 6:
            break
        contador += 1
    exibePartida(termo_lista)

    if contador == 6:
        mostrar(f'A palavra era {termo_palavra} :(', '~')
    else:
        mostrar(f'{contador}º jogada :)', '~')


def mudarModo():
    pass


def novoIdioma():
    from dados.config import Idioma

    limpaTerminal()
    
    IDIOMAS = ('pt_br', 'en')

    while True:
        print('Escolha um dos idiomas: ')
        for idioma in IDIOMAS:
            print(f'{cores(idioma, "Azul")}', end='')
            if idioma == IDIOMAS[-1]:
                print()
            else:
                print(', ', end='')
        idioma_novo = str(input('>>> Sua opção: '))
        if idioma_novo in IDIOMAS:
            Idioma = idioma_novo
            return Idioma
        else:
            print(cores('Digite um valor válido', 'Vermelho'))


def mudarTema():
    pass


def sair():
    from sys import exit

    limpaTerminal()
    mostrar('Volte Sempre!', '-', 30)
    exit()
