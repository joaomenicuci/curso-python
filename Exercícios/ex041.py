# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM. – Até 14 anos: INFANTIL. – Até 19 anos: JÚNIOR. – Até 25 anos: SÊNIOR. – Acima de 25 anos: MASTER.

from datetime import date

atual = date.today().year
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - ano

print('Um atleta que nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 25:
    print('A sua categoria é: MASTER')
elif 19 < idade <= 25:
    print('A sua categoria é: SÊNIOR')
elif 14 < idade <= 19:
    print('A sua categoria é: JÚNIOR')
elif 9 < idade <= 14:
    print('A sua categoria é: INFANTIL')
else:
    print('A sua categoria é: MIRIM')
