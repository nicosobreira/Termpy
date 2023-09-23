from lib.strings import *


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


def novoJogo():
    from data.config import Modo
    from lib.modos import termoJogo, duetoJogo

    if Modo == 'termo':
        termoJogo()
    elif Modo == 'dueto':
        duetoJogo()


def novoIdioma():
    from data.config import Idioma
    IDIOMAS = ('pt_br', 'en')

    limpaTerminal()

    while True:
        limpaTerminal()
        print('Escolha um dos idiomas: ')
        exibeTupla(IDIOMAS)
        novo_idioma = str(input('>>> Sua opção: '))
        if novo_idioma in IDIOMAS:
            Idioma = novo_idioma
            return Idioma
        else:
            print(cores('Digite um valor válido', 'Vermelho'))


def sair():
    from sys import exit

    limpaTerminal()
    mostrar('Volte Sempre!', '-', 30)
    exit()
