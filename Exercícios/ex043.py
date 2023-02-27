# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: – IMC abaixo de 18,5: Abaixo do Peso. – Entre 18,5 e 25: Peso Ideal. – 25 até 30: Sobrepeso. – 30 até 40: Obesidade. – Acima de 40: Obesidade Mórbida.

peso = float(input('Qual o seu peso em Kilos? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura**2)
print('Com uma altura de {:.2f}m e um peso de {:.2f}Kg, seu IMC é: {:.2f}.'.format(altura, peso, imc))
if imc < 18.5:
    print('Você está Abaixo do Peso.')
elif 18.5 < imc < 25:
    print('Você está no Peso Ideal.')
elif 25 < imc < 30:
    print('Você está com Sobrepeso.')
elif 30 < imc < 40:
    print('Você está com Obesidade.')
else:
    print('Você está com Obesidade Mórbida.')
