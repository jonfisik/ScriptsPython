''' Jonatan Paschoal 11/05/2020 - Crie um programa que receba nome de cidades e verifique se começa com a palavra Santo'''

print('---------------'*3)
cidade = input('Digite o nome de uma cidade: ')
#------------------------------------------------------------
x = cidade.split()
#-------------------------------------------------------------
a = (x[0])
#-------------------------------------------------------------
print('O nome da cidade começa com - {}.'.format(a.capitalize()))

print('---------------'*3)