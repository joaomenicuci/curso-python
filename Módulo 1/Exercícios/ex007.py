# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
m = (n1+n2)/2

print('A nota da primeira prova é {:.2f}, e da segunda prova é {:.2f}. A sua média final é {:.2f}.'.format(n1, n2, m))
