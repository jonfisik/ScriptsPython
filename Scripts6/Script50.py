'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. 03/07/2020'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('SOMA PARES')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
somador = 0
cont = 0
for c in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        somador += n
        cont += 1 # cont = cont + 1
        print('-----'*10)
    else:
        print('-----'*10)
        print('>> {} << não é par.'.format(n))
        print('-----'*10)
print('Você nos informou {} pares.'.format(cont))
print('A soma dos pares é >> {} <<.'.format(somador))