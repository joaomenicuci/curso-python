#   Funções - Parte 1
    # Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
    # Definimos uma função com o comando:   def:

#   Exercício 1

def titulo(txt):
    print('-'*50)
    print(txt)
    print('-'*50)


titulo('    CURSO DE PYTHON     ')
titulo('    APRENDA PYTHON      ')
titulo('    JOÃO LUCAS MENICUCI     ')

#   Exercício 2

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(4, 5)
soma(8, 9)
soma(2, 1)

#   Exercício 3

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(valor, end=' ')
    print('Fim')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#   Exercício 4

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#   Exercício 5

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
