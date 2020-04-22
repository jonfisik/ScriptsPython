'''Desafio 05 e 06 - Parte 1 Monte um progrma que receba um valor e mostre seu antecessor e seu sucessor. Parte 2 Calcule o dobro o triplo e a raíz quadrada do número digitado. Jonatan Paschoal 22/04/2020'''
print('-------------------------------')
a = ('Digite um número inteiro.')
print('{:^30}'.format(a))
x = int(input('  x = '))
#-------------------------------------
antecessor = x - 1
sucessor = x + 1
#-------------------------------------
dobro = 2*x
triplo = 3*x
raiz = (x)**(0.5)
#-------------------------------------
print('  Antecessor de {} é {}.'.format(x, antecessor))
print('  Sucessor de {} é {}.'.format(x, sucessor))
print('  O dobro de {} é {}.'.format(x, dobro))
print('  O triplo de {} é {}.'.format(x, triplo))
print('  A raiz quadrade de {} é {:.2f}.'.format(x, raiz))
print('-------------------------------')