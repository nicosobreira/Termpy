# Formatação - ~/Termpy/formatação/__init__.py


def exibePartida(lista, partida):
    limpaTerminal()
    mostrar(f' -- Termpy, {partida}ª partida --', '~', 30)

    for índex, elemento in enumerate(lista):
        índex += 1
        print(f'{elemento} - {cores(índex, "Azul")}')


def linha(tipo_linha='-', tamanho_linha=30):
    return tipo_linha * tamanho_linha


def mostrar(texto='', tipo='-', tamanho=30):
    linha_ver = linha(tipo, tamanho)
    print(linha_ver)
    print(texto.center(tamanho))
    print(linha_ver)


def cores(texto, cor):
    CORES = {
        'Normal': '\033[m',
        'Verde': '\033[32m',
        'Amarelo': '\033[33m',
        'Vermelho': '\033[31m',
        'Azul': '\033[34m'
    }

    return f"{CORES[cor]}{texto}{CORES['Normal']}"


def limpaTerminal():
    import os

    if os.name == 'posix':  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:
        pass


def tutorial():
    from time import sleep

    linha_str = linha('-')
    print(linha_str)
    print(' - ' + cores('Correto', 'Verde'))
    print(' - ' + cores('Meio Certo', 'Amarelo'))
    print(' - ' + cores('Errado', 'Vermelho'))
    print(linha_str)
    sleep(1)


def continuação(caminho):
    while True:
        print('Esse é o caminho: ' + caminho)
        continuação = str(input('Deseja continuar? [S/N] '))
        if continuação in 'Ss':
            return True


"""
def removeAcento(texto):
    ACENTOS = {
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A',
        'É': 'E', 'Ê': 'E', 'È': 'E',
        'Í': 'I', 'Î': 'I', 'Ì': 'I',
        'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ò': 'O',
        'Ú': 'U', 'Û': 'U', 'Ù': 'U',
        'Ç': 'C'
    }
    tabela_tradução = str.maketrans(ACENTOS)
    sem_acentos = texto.translate(tabela_tradução)

    return sem_acentos
"""
