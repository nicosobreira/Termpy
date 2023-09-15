def cores(texto='', cor='Normal'):
    CORES = {
        'Normal': '\033[m',
        'Verde': '\033[33m',
        'Amarelo': '\033[32m',
        'Vermelho': '\033[31m'
    }

    return f"{CORES[cor]}{texto}{CORES['Normal']}"


def continuação(caminho):
    while True:
        print('Esse é o caminho: ' + caminho)
        continuação = str(input('Deseja continuar? [S/N] '))
        if continuação in 'Ss':
            return True
