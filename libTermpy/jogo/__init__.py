# Jogo - ~/Termpy/jogo/__init__.py

from libTermpy.formatação import *


def geradorTermo():
    from random import choice
    from bancoDados.termos import TERMOS

    return choice(TERMOS)


def jogo(usr_palavra, termo_palavra):
    usr_termo_list = []

    for índex, letra in enumerate(usr_palavra):
        if letra in termo_palavra:
            if índex == termo_palavra.find(letra):
                letra_cor = cores(letra, 'Verde')
            else:
                letra_cor = cores(letra, 'Amarelo')
        else:
            letra_cor = cores(letra, 'Vermelho')
        print(letra_cor, end='')
        usr_termo_list.append(letra_cor)
    print()
    usr_termo_str = ' '.join(usr_termo_list)
    return usr_termo_str
