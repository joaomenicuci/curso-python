# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas, Quantas letras ao todo (sem considerar espaços) e Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em minúsculo fica: {}'.format(nome.lower()))
print('Seu nome em maiúsculo fica: {}'.format(nome.upper()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
