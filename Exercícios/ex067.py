# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*35)
    for c in range(1, 11):
        print(f'{n} x {c} = {(n*c)}')
    print('-'*35)
print('Programa encerrado.')
