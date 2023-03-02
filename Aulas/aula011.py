#   Cores no Terminal
    # Style: 0 (none), 1 (negrito), 4 (sublinhado), 7 (negativo)
    # Text: 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (roxo), 36 (ciano), 37 (cinza)
    # Back: 40 (branco), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (azul), 45 (roxo), 46 (ciano), 47 (cinza)
    # Começar utilizando barra invertida, 033 e abrir colchetes, e finalizar com m. (\033[...m)
    # Exemplo: \033[1:33:44m - negrito, texto em amarelo e fundo em azul.

#   Exercício 1

print('\033[1:31:43m Olá, Mundo\033[m')

#   Exercício 2

print('\033[4:34:47m Olá, Mundo\033[m')

#   Exercício 3

print('\033[7:33:44m Olá, Mundo\033[m')
