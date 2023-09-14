from lib.pastas import *


bancoDados_caminho = bancoDadosUsuário()
formatado_caminho = formatadoPergunta()


with open(formatado_caminho, 'a') as formatado:
    formatado.write('ANALISADOS = (')


linhas_termos = []
with open(bancoDados_caminho, 'r+') as bancoDados:
    LINHAS = bancoDados.readlines()
    for linha in LINHAS:
        linha = linha.strip().upper()
        if len(linha) == 5:
            linhas_termos.append(linha)


with open(formatado_caminho, 'a+') as formatado:
    for linha in linhas_termos:
        formatado.write(f"'{linha}'")
        if linha == linhas_termos[-1]:
            formatado.write(')')
        else:
            formatado.write(', ')


print('Finalizado!')
print('Arquivo criado com sucesso')
print('Volte Sempre!')
