# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = float(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos Km foram rodados com o carro? '))
p = ((d*60)+(k*0.15))

print('O carro foi alugado por {} dia(s) e rodou {}Kms. O valor total a se pagar é R${}'.format(d, k, p))
