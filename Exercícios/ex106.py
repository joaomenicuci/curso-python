# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

#   Biblioteca de Cores

c = (   '\033[m',           # 0 - Sem Cores
        '\033[0;30;41m',    # 1 - Vermelho
        '\033[0;30;42m',    # 2 - Verde
        '\033[0;30;43m',    # 3 - Amarelo
        '\033[0;30;44m',    # 4 - Azul
        '\033[0;30;45m',    # 5 - Roxo
        '\033[7;30m'         # 6 - Branco
    );

#   Funções

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print()
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tamanho = len(msg) + 10
    print(c[cor], end='')
    print('-' * tamanho)
    print(f'     {msg}     ')
    print('-' * tamanho)
    print(c[0], end='')
    sleep(1)

#   Programa Principal

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON', 3)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM' or comando.upper() == 'QUIT' or comando.upper() == 'EXIT':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
