# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

num = int(input('Qual o número inteiro você gostaria de converter: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print('{} em binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em hexadecimal é: {}'.format(num, hex(num)[2:].upper()))
else:
    print('Por favor, escolha uma das opções disponíveis. [ 1 ], [ 2 ] ou [ 3 ]')
