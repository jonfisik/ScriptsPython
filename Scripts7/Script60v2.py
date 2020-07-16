''''fatorial por função'''
from math import factorial
num = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num,f))