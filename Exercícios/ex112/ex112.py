# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex112.packutilidades import moeda
from ex112.packutilidades import dado

preço = dado.leiaDinheiro('Digite o preço: R$')
taxaA = float(input('Qual a taxa de juros você quer (valor em %)? '))
taxaR = float(input('Qual a taxa de desconto você quer (valor em %)? '))
moeda.resumo(preço, taxaA, taxaR)
