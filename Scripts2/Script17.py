'''Faça um programa que leia o comprimento dos catetos de um triângulo retângulo, calcule e mostre o comprimento da hipotenuza.'''
print('====='*10)
print('Digite apenas valores inteiros.')
cat1 = int(input('Digite o valor do primeiro cateto: '))
cat2 = int(input('Digite o valor do segundo cateto: '))
hip = ((cat1**2)+(cat2**2))**(1/2)
print('A hipotenusa é {}.'.format(hip))
print('====='*10)