# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: – Média abaixo de 5.0: REPROVADO. – Média entre 5.0 e 6.9: RECUPERAÇÃO. – Média 7.0 ou superior: APROVADO.

n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
media = (n1+n2)/2

if media >= 7:
    print('APROVADO! Você ficou com {:.2f} de média.'.format(media))
elif 5 < media < 6.99:
    print('RECUPERAÇÃO! Você ficou com {:.2f} de média.'.format(media))
else:
    print('REPROVADO! Você ficou com {:.2f} de média.'.format(media))
