'''Dsenvolva um programa que leia 3 segmentos de reta e verifique se pode formar um triângulo.'''
from time import sleep
print('=+=+=+=+=+=+=+=+='*3)
titulo = ('Teste de existência do triangulo.')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
msn = """Para construir um triângulo não podemos\nutilizar qualquer medida, tem que seguir a condição\nde existência: é necessário que a medida de qualquer\num dos lados seja menor que a soma das medidas dos\noutros dois e maior que o valor absoluto da\ndiferença entre essas medidas."""
print('{:^}'.format(msn))
print('-----------------'*3)
print('Digite 3 medidas dos lados de um triângulo.')
print('-----------------'*3)
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))
print('-----------------'*3)
#----------------Área de teste---------------------
#lado1
print('TESTANDO lado 1...')
sleep(2)
x = lado2 + lado3
y = abs(lado2 - lado3)
if lado1 < x and lado1 > y:
    print('{} + {} = {}'.format(lado2,lado3,x))
    print('{} - {} = {}'.format(lado2,lado3,y))
    print('{} > {} > {}'.format(x,lado1,y))
    print('Teste 1 ok')
else:
    print('{} + {} = {}'.format(lado2,lado3,x))
    print('{} - {} = {}'.format(lado2,lado3,y))
    print('Lado: {}.'.format(lado1))
    print('Falha no teste 1.')
print('-----------------'*3)
#lado2
print('TESTANDO lado 2...')
sleep(2)
x = lado1 + lado3
y = abs(lado1 - lado3)
if lado2 < x and lado2 > y:
    print('{} + {} = {}'.format(lado1,lado3,x))
    print('{} - {} = {}'.format(lado1,lado3,y))
    print('{} > {} > {}'.format(x,lado2,y))
    print('Teste 2 ok')
else:
    print('{} + {} = {}'.format(lado1,lado3,x))
    print('{} - {} = {}'.format(lado1,lado3,y))
    print('Lado: {}.'.format(lado2))
    print('Falha no teste 2.')
print('-----------------'*3)
#lado3
print('TESTANDO lado 3...')
sleep(2)
x = lado2 + lado1
y = abs(lado2 - lado1)
if lado3 < x and lado3 > y:
    print('{} + {} = {}'.format(lado1,lado2,x))
    print('{} - {} = {}'.format(lado1,lado2,y))
    print('{} > {} > {}'.format(x,lado3,y))
    print('Teste 3 ok')
else:
    print('{} + {} = {}'.format(lado1,lado2,x))
    print('{} - {} = {}'.format(lado1,lado2,y))
    print('Lado: {}.'.format(lado3))
    print('Falha no teste 3.')
print('-----------------'*3)
if ((lado2+lado3) > lado1 and lado1 > abs(lado2-lado3)) and ((lado1+lado3) > lado2 and lado2 > abs(lado1-lado3)) and ((lado2+lado1) > lado3 and lado3 > abs(lado1-lado1)):
    print('As medidas [{}], [{}] e [{}] formam um triângulo.'.format(lado1,lado2,lado3))
else:
    print('As medidas [{}], [{}] e [{}] não formam um triângulo.'.format(lado1,lado2,lado3))
print('=+=+=+=+=+=+=+=+='*3)