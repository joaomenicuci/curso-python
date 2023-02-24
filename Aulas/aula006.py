#   Tipos Primitivos
    #   Tipos:  int(), float(), bool(), str()

#   Exercício 1

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} vale: {}'.format(n1, n2, s))

#   Exercício 2

# n = float(input('Digite um valor: '))
n = (input('Digite algo: '))

# print(n.isnumeric())
# print(n.isalpha())
print(n.isalnum())
