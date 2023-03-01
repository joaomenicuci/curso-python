# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-'*50)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
