# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-='*14)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-='*14)

if computador  == 0:    # Pedra
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada Inválida! Tente novamente!')

elif computador == 1:   # Papel
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada Inválida! Tente novamente!')
    
elif computador == 2:   # Tesoura
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada Inválida! Tente novamente!')
