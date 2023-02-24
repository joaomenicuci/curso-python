# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l*h

print('A sua parede tem uma dimensão de {}x{} e sua área é de {:.2f}m²'.format(l, h, a))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta'.format((a/2)))
