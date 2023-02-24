# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math
angulo = float(input('Digite o ângulo que você deseja: '))
ang = math.radians(angulo)

print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, math.sin(ang)))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, math.cos(ang)))
print('O ângulo de {} tem a Hipotenusa de {:.2f}'.format(angulo, math.tan(ang)))
