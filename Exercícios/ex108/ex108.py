# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import ex108functions

preço = float(input('Digite o preço do produto: R$'))
print(f'A metade de {ex108functions.moeda(preço)} é {ex108functions.moeda(ex108functions.metade(preço))}.')
print(f'O dobro de {ex108functions.moeda(preço)} é {ex108functions.moeda(ex108functions.dobro(preço))}.')
taxa = float(input('Qual a taxa de juros ou desconto você quer (valor em %)? '))
print(f'Com desconto de {taxa}%, o valor fica: {ex108functions.moeda(ex108functions.diminuir(preço, taxa))}.')
print(f'Com aumento de {taxa}%, o valor fica: {ex108functions.moeda(ex108functions.aumentar(preço, taxa))}.')
