# Formatação - ~/Termpy/formatação/__init__.py


def errorMensagem(mensagem):
    mensagem = f'ERROR! {mensagem}'
    mostrarTexto(coloreTexto(mensagem, 'Vermelho'))


def linha(tipo_linha='-', tamanho_linha=30):
    print(tipo_linha * tamanho_linha)


def mostrarTexto(texto, tipo='-', tamanho=30):
    if len(texto) > tamanho and tamanho == 30:
        custom_tamanho = len(texto) + 2
        linha(tipo, custom_tamanho)
        print(texto.center(custom_tamanho))
        linha(tipo, custom_tamanho)
    else:
        linha(tipo, tamanho)
        print(texto.center(tamanho))
        linha(tipo, tamanho)



def coloreTexto(texto, cor='Normal'):
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
    cor = cor.capitalize()
    return f"{CORES[cor]}{texto}{CORES['Normal']}"


def limpaTerminal():
    from os import system, name

    if name == 'posix':  # Para sistemas Unix/Linux/Mac
        system('clear')
    elif name == 'nt':  # Para sistemas Windows
        system('cls')
    else:
        pass


def mostraLista(lista):
    for índex, elemento in enumerate(lista):
        print(f'{índex + 1} - {coloreTexto(elemento, "Azul")}')
