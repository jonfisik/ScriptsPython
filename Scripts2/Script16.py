'''Crie um programa que leia um número real qualquer pelo teclado e mostre sua porção inteira.'''
print('==='*20)
a = float(input('Digite um número qualquer: '))
b = float(input('Digite outro número qualquer: '))

x = a//b

print('A parte inteira da divisão de {} por {} é >> {} <<'.format(a,b,int(x)))
print('==='*20)