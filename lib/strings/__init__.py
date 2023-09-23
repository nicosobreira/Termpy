# Formatação - ~/Termpy/formatação/__init__.py


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
        'Azul': '\033[34m',
        'Roxo': '\033[35m',
        'Ciano': '\033[36m',
        'Cinza': '\033[37m'
    }

    return f"{CORES[cor]}{texto}{CORES['Normal']}"


def limpaTerminal():
    from os import system, name

    if name == 'posix':  # Para sistemas Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # Para sistemas Windows
        system('cls')
    else:
        pass


def exibeTupla(tupla):
    for elemento in tupla:
        print(f'{cores(elemento, "Azul")}', end='')
        if elemento == tupla[-1]:
            print()
        else:
            print(', ', end='')
