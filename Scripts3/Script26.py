''' Jonatan Paschoal 11/05/2020 - Crie um programa que receba uma frase e conte quantas vezes a aparecem a letra 'a', qual a primeira posição e última posição que ela aparece.'''

print('---------------'*3)
frase = input('Digite uma frase: ')
#------------------------------------------------------------
x = frase.lower() 
y = x.count('a')
z = x.find('a') + 1
#-------------------------------------------------------------
print('Número de vezes que aparece a letra "a": {}.'.format(y))
print('Primeira posição que aparece a letra "a": {}.'.format(z))
print('---------------'*3)