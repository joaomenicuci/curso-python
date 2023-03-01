# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    r = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if r in 'N':
        break
print('-'*50)
num.sort()
print(f'Você digitou os valores {num}')
