# Jogo - ~/Termpy/jogo/__init__.py

from lib.strings import cores
from lib.pastas import diretórioAtual

def escolhaIdioma():
    IDIOMAS = ('pt_br', 'en')

    while True:
        print('Escolha um dos idiomas: ')
        for idioma in IDIOMAS:
            print(f'{cores(idioma, "Azul")}', end='')
            if idioma == IDIOMAS[-1]:
                print()
            else:
                print(', ', end='')
        idiomaUsuário = str(input('>>> Sua opção: '))
        if idiomaUsuário in IDIOMAS:
            break
        else:
            print(cores('Digite um valor válido', 'Vermelho'))

    return str(idiomaUsuário)


def geradorTermo(idioma):
    from random import choice
    import importlib.util
    
    caminho = f'{diretórioAtual()}/dados/formatado/{idioma}'
    
    # Usa o importlib.util.spec_from_file_location
    # para criar um novo módulo
    spec = importlib.util.spec_from_file_location(idioma, caminho)
    modulo = importlib.util.module_from_spec(spec)

    # Carrega o módulo
    spec.loader.exec_module(modulo)

    return choice(modulo.TERMOS)


def perguntaTermo(texto=''):
    while True:
        usr_input = str(input(texto)).upper()
        if len(usr_input) != 5:
            print(cores('ERRO! 5 dígitos apenas', 'Vermelho'))
        else:
            return usr_input


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
    return usr_termo_str
