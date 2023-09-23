# Jogo - ~/Termpy/jogo/__init__.py

from lib.strings import cores
from lib.pastas import diretórioAtual


def geradorTermo():
    from data.config import Idioma

    from random import choice
    import importlib.util

    idioma = f'{Idioma}_termos.py'
    caminho = f'{diretórioAtual()}/data/formatado/{idioma}'

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


def jogoResultadoLista(usr_termo, termo_geradorTermo):
    usr_termo_list = []

    for índex, letra in enumerate(usr_termo):
        if letra in termo_geradorTermo:
            if índex == termo_geradorTermo.find(letra):
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


def exibePartida(jogo_lista):
    from lib.strings import limpaTerminal, mostrar

    limpaTerminal()
    mostrar(f' -- Termpy, Termo --', '~', 30)

    for índex, elemento in enumerate(jogo_lista):
        índex += 1
        print(f'{elemento} - {cores(índex, "Azul")}')
