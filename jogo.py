from lib.menu import *
import dados.config as config

def perguntaMenu():
    opçõesPossíveis = ('N', 'M', 'I', 'T', 'S')

    while True:
        mostrar(f'''Você deseja...
Nn - Nova partida
Mm - Trocar de Modo ["{config.Modo}"] (Ainda Fazer)
Ii - Novo Idioma ["{config.Idioma}"]
Tt - Trocar de Tema ["{config.Tema}"] (Ainda Fazer)
Ss - Sair''')
        opção_usuário = str(input('>>> Sua opção: ')).upper()
        if opção_usuário in opçõesPossíveis:
            return opção_usuário


def menu(opçãoUsuário):
    match opçãoUsuário:
        case 'N':  # Novo Jogo
            novoJogo(config.Idioma)
        case 'M':  # Mudar modo de jogo
            print(config.Modo)
        case 'I':  # Novo Idioma
            idioma_usuário = novoIdioma()
            config.Idioma = idioma_usuário
            novoJogo(config.Idioma)
        case 'T':  # Troca de Tema
            print(config.Tema)
        case 'S':  # Sair
            sair()


while True:
    opção_usuário = perguntaMenu()
    menu(opção_usuário)
