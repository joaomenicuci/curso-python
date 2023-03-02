# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área do terreno é de {a} metros.')


print('Controle de Terrenos')
print('-'*50)
l = float(input('Digite a Largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))
area(l, c)
