# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*40)
print('     10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)

i = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
f = i + (10*r)

for c in range(i, f, r):
    print('{}'.format(c), end=' → ')
print('Acabou')
