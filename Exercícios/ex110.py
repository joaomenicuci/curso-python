# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import ex110functions

preço = float(input('Digite o preço do produto: R$'))
taxaA = float(input('Qual a taxa de juros você quer (valor em %)? '))
taxaR = float(input('Qual a taxa de desconto você quer (valor em %)? '))
ex110functions.resumo(preço, taxaA, taxaR)
