#   Módulos e Pacotes
    # Modularização: dividir um programa grande em pequenos pedaços, e isso aumenta a legibilidade.
    # Pacotes: são conjuntos de módulos de funções.

#   Exercício 1

import aula022functions

num = int(input('Digite um valor: '))
fat = aula022functions.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {aula022functions.dobro(num)}')
print(f'O triplo de {num} é {aula022functions.triplo(num)}')
