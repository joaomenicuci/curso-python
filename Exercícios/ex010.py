# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

n = float(input('Quanto de dinheiro você tem na carteira? R$'))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, (n/5.14)))
