'''Faça um programa que faça um ângulo qualquer e calcule o seno, coseno e a tangente'''
from math import sin
from math import cos
from math import tan
from math import pi
print('------'*5)
grau = int(input(' Qual o valor do ângulo? '))

rad = (grau*pi) / 180
x = sin(rad)
y = cos(rad)
z = tan(rad)
print(' seno - {:.2f}\n cosseno - {:.2f}\n tangente {:.2f}'.format(x,y,z))
print('------'*5)