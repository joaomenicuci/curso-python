#   Funções - Parte 2
    # Interactive Help:     help()
    # docstrings (String de Documentação): Documentação criada para funções personalizadas. Definir a documentação abaixo do def e colocara entre 3 aspas duplas (""" """).
    # Argumentos Opcionais: Valores opcionais em uma função personalizada. Necessário definir no desenvolvimento da função.
    # Escopo de Variáveis: Variáveis Globais valem em todo o programa (Escopo Global). Variáveis Locais valem apenas em locais específicos, como dentro de funções (Escopo Local).
    # Retorno de Resultados: Retorna uma resposta para dentro de uma variável ou para dentro de um print. Utilizar o comando return na criação da função.

#   Exercício 1

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

#   Exercício 2

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
