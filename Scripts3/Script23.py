''' Jonatan Paschoal 11/05/2020 - Crie um programa que leia um número de 0 9999 e mostre na tela cada um dos seus dígitos separados por unidade, dezena, centena e milhar. '''
print('---------------'*3)
print('O número deve ter o formato de quatro dígitos.')
numero = input('Digite um número inteiro de 0 a 9999: ')
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
print('Rsolução alternativa')
# Resoluçaõ alternativa
print('O número deve ter até 4 dígitos.')
num = int(input('Informe um número: '))
unid = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
#---------------------------------------------------------------
print('Analisando o número: {}...'.format(num))
print('Unidade: {}.'.format(unid))
print('Dezena: {}.'.format(dez))
print('Centena: {}.'.format(cen))
print('Milhar: {}.'.format(mil))
print('---------------'*3)