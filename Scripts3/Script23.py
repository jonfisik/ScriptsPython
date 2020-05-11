''' Jonatan Paschoal 11/05/2020 - Crie um programa que leia um número de 0 9999 e mostre na tela cada um dos seus dígitos separados por unidade, dezena, centena e milhar. '''
import math

print('---------------'*3)
numero = input('Digite um número inteiro de 0 a 9999: ')
print('O número deve ter o formato de quatro dígitos.')
#------------------------------------------------------------
x = numero.split()
#-------------------------------------------------------------
a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
d = int(numero[3])
#-------------------------------------------------------------
print('Número digitado - {}.'.format(numero))
print('Unidade: {}.'.format(d))
print('Dezenas: {}.'.format(c))
print('Centenas: {}.'.format(b))
print('Milhar: {}.'.format(a))
print('---------------'*3)