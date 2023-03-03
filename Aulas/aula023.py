#   Tratamento de Erros e Exceções
    # Comandos try, except, else e finally para tentar identificar e responder erros.
    # Um try pode ter inúmeros except.
    # Os comandos else e finally são opcionais.

#   Exercício 1
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado é {r:.2f}.')
finally:
    print('Volte sempre! Muito obrigado!')
