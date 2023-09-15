from libAnalisador.pastas import *


def main():
    bancoDados_caminho = bancoDadosUsuário()
    formatado_caminho = formatadoPergunta()

    with open(bancoDados_caminho, 'r') as bancoDados_arquivo, open(formatado_caminho, 'a+') as formatado_arquivo:  # r+ -> r
        formatado_arquivo.write('ANALISADOS = (')

        bancoDados_LINHAS = bancoDados_arquivo.readlines()
        bancoDados_TERMOS = []
        for linha in bancoDados_LINHAS:
            linha = linha.strip().upper()
            if len(linha) == 5:
                bancoDados_TERMOS.append(linha)

        for termo in bancoDados_TERMOS:
            if termo == bancoDados_TERMOS[-1]:
                escrever = ')'
            else:
                escrever = ', '
            formatado_arquivo.write(f"'{termo}'{escrever}")


if __name__ == '__main__':
    main()

    print('Finalizado!')
    print('Arquivo criado com sucesso')
