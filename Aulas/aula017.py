#   Variáveis Compostas - Listas
    # As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
    # Listas são definidas entre colchetes [].

#   Exercício 1

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

#   Exercício 2

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei no final da lista.')

#   Exercício 3

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei no final da lista.')


#   Exercício 4

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
