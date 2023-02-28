# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0, 10)
print('-=' * 28)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=' * 28)

palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('O número é maior. Tente mais uma vez.')
        else:
            print('O número é menor. Tente mais uma vez.')
print('Você acertou com {} palpites.'.format(palpites))
