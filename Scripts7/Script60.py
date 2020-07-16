'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
print('-----------'*3)
titulo = 'FATORIAL'
print('{:^30}'.format(titulo))
print('-----------'*3)
num = int(input('''Digite um número
para calcular seu fatorial: '''))
x = 1
while x < num:
     for x in range(1, num):
         num = x * num
         print(num) 