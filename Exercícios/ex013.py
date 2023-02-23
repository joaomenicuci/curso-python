# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n = float(input('Qual o seu salário? R$'))
print('O seu salário é R${:.2f}. Com um aumento de 15%, seu salário será R${:.2f}'.format(n, (n*1.15)))
