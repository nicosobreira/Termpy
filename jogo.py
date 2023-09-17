from lib.menu import *


def perguntaMenu():
    opçõesPossíveis = ('N', 'M', 'I', 'T', 'S')

    while True:
        mostrar('''Você deseja...
    Nn - Nova partida
    Mm - Trocar de Modo (Ainda Fazer)
    Ii - Novo Idioma [padrão pt_br](Ainda fazer)
    Tt - Trocar de Tema (Ainda Fazer)
    Ss - Sair''')
        opção_usuário = str(input('>>> Sua opção: ')).upper()
        if opção_usuário in opçõesPossíveis:
            return opção_usuário


def menu(opçãoUsuário):
    match opçãoUsuário:
        case 'N':  # Novo Jogo
            novoJogo('pt_br')
        case 'M':  # Mudar modo de jogo
            print('M')
        case 'I':  # Novo Idioma
            idioma_usuário = escolhaIdioma()
            novoJogo(idioma_usuário)
        case 'T':  # Troca de Tema
            print('T')
        case 'S':  # Sair
            sair()

while True:
    opção_usuário = perguntaMenu()
    if opção_usuário == 'S':
        menu('S')
        break
    menu(opção_usuário)
