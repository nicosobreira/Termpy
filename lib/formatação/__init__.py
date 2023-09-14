# Formatação - ~/Termpy/formatação/__init__.py

def palavrasCaps(palavras):
    for p in palavras:
        print(f'"{p.upper()}", ', end='')


def pergunta(texto=''):
    while True:
        usr_input = str(input(texto)).upper()
        if len(usr_input) != 5:
            print(cores('ERRO! 5 dígitos apenas', 'Vermelho'))
        else:
            return usr_input


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
        'Verde': '\033[33m',
        'Amarelo': '\033[32m',
        'Vermelho': '\033[31m'
    }

    return f"{CORES[cor]}{texto} {CORES['Normal']}"


def limparTerminal():
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
    sleep(1.5)


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
