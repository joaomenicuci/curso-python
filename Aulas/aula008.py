#   Utilizando Módulos
    #   Módulos são conhecidos como Bibliotecas
    #   Adicionamos bibliotecas utilizando o comando IMPORT e/ou FROM
    #   import XXXX             - Importação generalizada
    #   from XXXX import YYYY   - Importação específica

#   Exercício 1

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é: {:.2f}'.format(num, raiz))

#   Exercício 2

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é: {:.2f}'.format(num, raiz))
