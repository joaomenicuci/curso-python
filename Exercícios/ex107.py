# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import ex107functions

preço = float(input('Digite o preço do produto: R$'))
print(f'A metade do preço é R${ex107functions.metade(preço)}.')
print(f'O dobro do preço é R${ex107functions.dobro(preço)}.')
taxa = float(input('Qual a taxa de juros ou desconto você quer (valor em %)? '))
print(f'Com desconto de {taxa}%, o valor fica: R${ex107functions.diminuir(preço, taxa)}.')
print(f'Com aumento de {taxa}%, o valor fica: R${ex107functions.aumentar(preço, taxa)}.')
