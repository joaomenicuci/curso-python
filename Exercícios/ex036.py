# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
meses = anos*12
prest = casa/meses

print('Para pagar uma casa de {:.2f} em {} anos, a prestação mensal será de {:.2f}.'.format(casa, anos, prest))
if prest >= (0.3*salário):
    print('Infelizmente não podemos te liberar o empréstimo porque a prestação mensal comprometeria mais de 30% da sua renda. ')
else:
    print('Seu empréstimo foi aprovado! Você irá pagar R${:.2f} por {} meses.'.format(prest, meses))
print('Obrigado!')
