# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], [media]])
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp in 'N':
        break
print('-'*50)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>10}')
print('-'*50)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<15}{a[2]}')
while True:
    print('-'*50)
    opc = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
