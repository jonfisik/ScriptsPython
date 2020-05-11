''' Jonatan Paschoal 11/05/2020 - Crie um programa que receba nome de uma pessoa e verifique se ela te silva'''

print('---------------'*3)
nome = input('Digite o seu nome: ')
#------------------------------------------------------------
x = nome.lower() 
y = 'silva' in x
#-------------------------------------------------------------
print('Para o nome Silva, temos {}. '.format(y))

print('---------------'*3)