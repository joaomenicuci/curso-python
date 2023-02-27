# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Qual o valor do produto? R$'))
print('O produto custa R${}. Com 5% de desconto o preço fica R${}'.format(n, (n*0.95)))
