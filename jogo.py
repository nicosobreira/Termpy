from lib.menu import *
import data.config as config

def perguntaMenu():
    OPÇÕES = ('N', 'I', 'S')

    limpaTerminal()
    while True:
        mostrar(f'''Você deseja...
N - Nova partida
I - Novo Idioma ["{config.Idioma}"]
S - Sair''')
        opção_usuário = str(input('>>> Sua opção: ')).upper()
        if opção_usuário in OPÇÕES:
            return opção_usuário


def menu(opçãoUsuário):
    if opçãoUsuário == 'N':
        novoJogo()
    elif opçãoUsuário == 'I':
        config.Idioma = novoIdioma()
    elif opçãoUsuário == 'S':
        sair()


while True:
    opção_usuário = perguntaMenu()
    menu(opção_usuário)
