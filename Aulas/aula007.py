#   Operações Aritméticas
    #   Adição (+), Subtração (-), Multiplicação (*), Divisão(/), Divisão Inteira (//), Resto da Divisão (%), Potência (**)

#   Ordem de Precedência
    #   Primeiro: () 
    #   Segundo: **
    #   Terceiro: *, /, //, %
    #   Quarto: +, -

#   Exercício 1

nome = input('Qual é seu nome? ')
print('Prazer em conhece-lo {}!'.format(nome))

#   Exercício 2

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, a multiplicação é {}, a divisão é {}, a divisão inteira é {} e a exponenciação é {}'.format(s, m, d, di, e))
