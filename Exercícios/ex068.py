# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    print('-'*50)
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-'*50)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            print('-'*50)
            v += 1
        else:
            print('Você perdeu!')
            print('-'*50)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            print('-'*50)
        else:
            print('Você perdeu!')
            print('-'*50)
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')