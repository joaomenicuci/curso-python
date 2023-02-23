# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
mm = m*1000
cm = m*100

print('{} metros equivalem a {} centímetros e {} milímetros'.format(m, cm, mm))
