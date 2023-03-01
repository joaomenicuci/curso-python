#   Variáveis Compostas - Listas Compostas
    # As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
    # Listas são definidas entre colchetes [].
    # É possível criar listas compostas, com listas dentro de listas.

#   Exercício 1

teste = list()
teste.append('João')
teste.append(28)
galera = list()
galera.append(teste[:])
teste[0] = 'Beatriz'
teste[1] = 25
galera.append(teste[:])
print(galera)

#   Exercício 2

galera = [['João', 28], ['Beatriz', 25], ['Mônica', 60], ['Antônio', 67]]
print(galera)
print(galera[0][0])
print(galera[1][0])

#   Exercício 3

galera = [['João', 28], ['Beatriz', 25], ['Mônica', 60], ['Antônio', 67]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#   Exercício 4

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in  galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
