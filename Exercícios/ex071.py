# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Observação: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10 e R$1.

print('='*50)
print('{:^50}'.format('BANCO MENICUCI'))
print('='*50)

valor = int(input('Qual valor você gostaria de sacar? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*50)
print('{:^50}'.format('VOLTE SEMPRE'))
print('='*50)
