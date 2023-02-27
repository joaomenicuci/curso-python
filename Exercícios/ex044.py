# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: – à vista dinheiro/PIX: 10% de desconto. – à vista no cartão: 5% de desconto. – em até 2x no cartão: preço formal. – 3x ou mais no cartão: 20% de juros.

print('=============== LOJAS MENICUCI ===============')

preço = float(input('Qual o valor total das compras? R$'))
print('''Qual a forma de pagamento?
[ 1 ] à vista no dinheiro ou PIX
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    print('Como você escolheu pagar no dinheiro ou PIX, iremos dar 10% de desconto.')
    print('O valor final ficará em R${:.2f}.'.format((0.9*preço)))
elif escolha == 2:
    print('Como você escolheu pagar no cartão à vista, iremos dar 5% de desconto.')
    print('O valor final ficará em R${:.2f}.'.format((0.95*preço)))
elif escolha == 3:
    print('Como você escolheu pagar em duas vezes no cartão, não conseguimos dar desconto.')
    print('O valor final ficará em R${:.2f}.'.format((preço)))
elif escolha == 4:
    print('Como você escolheu pagar em três vezes ou mais no cartão, irá ter acréscimo de 20% de juros.')
    print('O valor final ficará em R${:.2f}.'.format((1.20*preço)))
else:
    print('Por favor, escolha uma das opções disponíveis e tente de novo.')