#   Condições
    # Tipos de Condições:   if:, else:

#   Exercício 1

nome = str(input('Qual o seu nome? '))

if nome == 'João':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

#   Exercício 2

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média é {:.2f}'.format(m))

if m >= 5:
    print('Voc6e foi aprovado. Parabéns!')
else:
    print('Você está de recuperação. Estude mais!')

#   Exercício 3

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média é {:.2f}'.format(m))
print('Parabéns!' if m>=5 else 'Estude mais!')
