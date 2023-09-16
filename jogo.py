from lib.strings import *
from lib.jogo import *


partida = 0
continuação = ''


tutorial()
idioma_usuário = escolhaIdioma()
idioma_usuário = f'{idioma_usuário}_termos.py'
while True:
    partida += 1

    if continuação == 'R':
        pass
    else:
        termo_palavra = geradorTermo(idioma_usuário)

    contador = 1
    termo_lista = []
    while True:
        exibePartida(termo_lista, partida)
        usr_input_palavra = perguntaTermo('')
        jogada = jogoResultado(usr_input_palavra, termo_palavra)
        termo_lista.append(jogada)
        if usr_input_palavra == termo_palavra or contador == 6:
            break
        contador += 1
    exibePartida(termo_lista, partida)

    if contador == 6:
        mostrar(f'A palavra era {termo_palavra} :(', '~')
    else:
        mostrar(f'{contador}º jogada :)', '~')

    mostrar('''Você deseja...
    Nn - Nova partida
    Mm - Trocar de Modo (Ainda Fazer)
    Ii - Novo Idioma (Ainda fazer)
    Ss - Sair''')
    continuação = str(input('>>> Sua opção: ')).upper()
    if continuação == 'S':
        break

limpaTerminal()
mostrar('Volte Sempre!', '-', 30)
