'''Dsenvolva um programa que leia 3 segmentos de reta e verifique se pode formar um triângulo.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = ('Teste de existência do triangulo.')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
msn = """Para construir um triângulo não podemos\nutilizar qualquer medida, tem que seguir a condição\nde existência: é necessário que a medida de qualquer\num dos lados seja menor que a soma das medidas dos\noutros dois e maior que o valor absoluto da\ndiferença entre essas medidas."""
print('{:^}'.format(msn))
print('----------------------'*3)
print('Digite 3 medidas dos lados de um triângulo.')
print('----------------------'*3)
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))
#----------------Área de teste---------------------
#lado1
x = lado2 + lado3
y = abs(lado2 - lado3)
if lado1 < x and lado1 > y:
    print('Teste 1 ok')
#lado2
x = lado1 + lado3
y = lado1 - lado3
#lado3
x = lado2 + lado1
y = lado2 - lado1
print('=+=+=+=+=+=+=+=+='*3)