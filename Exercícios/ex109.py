# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import ex109functions

preço = float(input('Digite o preço do produto: R$'))
print(f'A metade de {ex109functions.moeda(preço)} é {(ex109functions.metade(preço, True))}.')
print(f'O dobro de {ex109functions.moeda(preço)} é {(ex109functions.dobro(preço, True))}.')
taxa = float(input('Qual a taxa de juros ou desconto você quer (valor em %)? '))
print(f'Com desconto de {taxa}%, o valor fica: {(ex109functions.diminuir(preço, taxa, True))}.')
print(f'Com aumento de {taxa}%, o valor fica: {(ex109functions.aumentar(preço, taxa, True))}.')
