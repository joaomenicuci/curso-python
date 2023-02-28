#   Variáveis Compostas - Tuplas
    # As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
    # Tuplas são definidas entre parenteses ().

#   Exercício 1

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

#   Exercício 2

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

#   Exercício 3

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Comi pra caramba!')

#   Exercício 4

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#   Exercício 5

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(sorted(lanche))

#   Exercício 6

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))

#   Exercício 7

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
