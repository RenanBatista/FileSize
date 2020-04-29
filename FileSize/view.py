import sys


class bcolors:
    DIRETORIO = '\033[94m'
    ARQUIVO = '\033[92m'
    ENDC = '\033[0m'


def filePrinter(nome, novoDestino, diretorioAtual, profundidade):
    sys.stdout.write('|')
    i = 0
    while(i < profundidade):
        sys.stdout.write('-')
        i += 1
    print(bcolors.DIRETORIO + novoDestino + "    " +
          diretorioAtual + '/' + novoDestino + bcolors.ENDC)
