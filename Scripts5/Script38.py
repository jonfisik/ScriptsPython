'''Faça um programa que receba dois números, compare e diga quem é maior. Mostrando a msn qual valor é maior ou menor. OU diga que os valores são iguais.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = 'COMPARANDO NÚMEROS MAIOR, MENOR E IGUAL'
print('{:^51}'.format(titulo))
print('-----------------'*3)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 == num2:
    print('Os números {} e {} são iguais.'.format(num1,num2))
elif num1 > num2:
    print('O número {} é \033[1;31mMAIOR\033[m que {}.'.format(num1, num2))
elif num1 < num2:
    print('O número {} é \033[1;34mMAIOR\033[m que {}.'.format(num2, num1))
else:
    print('Você precisa digitar um número. Tente novamente.')
print('=+=+=+=+=+=+=+=+='*3)
