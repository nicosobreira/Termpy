# Jogo - ~/Termpy/jogo/__init__.py

from lib.strings import cores
from lib.pastas import diretórioAtual


def geradorTermo(idioma_usuário):
    from random import choice
    import importlib.util

    idioma = f'{idioma_usuário}_termos.py'
    caminho = f'{diretórioAtual()}/dados/formatado/{idioma}'

    # Usa o importlib.util.spec_from_file_location para criar um novo módulo
    spec = importlib.util.spec_from_file_location(idioma, caminho)
    modulo = importlib.util.module_from_spec(spec)

    # Carrega o módulo
    spec.loader.exec_module(modulo)

    return choice(modulo.TERMOS)


def perguntaTermo(texto=''):
    while True:
        usr_termo = str(input(texto)).upper()
        if len(usr_termo) != 5:
            print(cores('ERRO! 5 dígitos apenas', 'Vermelho'))
        else:
            return usr_termo


def jogoResultado(usr_palavra, termo_palavra):
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
    ## print(type(jogoResultado)) ##
    return usr_termo_str
