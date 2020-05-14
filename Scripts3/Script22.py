''' Jonatan Paschoal 10/05/2020 - Crie um programa que leia o nome completo da pessoa e responda: 1 o nome com todas as letras maiúsculas 2 o nome com todas as letras minúsculas 3 quantas letras ao todo (sem contar os espaços) 4 - quantas letras tem o primeiro nome. '''
print('---------------'*3)
nome = input('Digite seu nome: ')
#------------------------------------------------------------
x = len(nome)
y = nome.count(' ')
LetrasTotal = x - y
#-------------------------------------------------------------
z = nome.split()
primeiro = len(z[0])
#-------------------------------------------------------------
print('Letras maiúsculas - {}'.format(nome.upper()))
print('Letras minúsculas - {}'.format(nome.lower()))
print('Total de letras - {}'.format(LetrasTotal))
print('Total de letras do primeiro nome - {}'.format(primeiro))
print('---------------'*3)

#resolução alternativa
nome = str(input('Digite seu nome: ')).strip() #strip elimina espaços a direita e a esquerda
print('Analisando nome...')
print('Nome em maiúsculo - {}'.format(nome.upper()))
print('Nome em minúsculo - {}'.format(nome.lower()))
print('Total de letras - {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#--------------------------------------------------------------
separa = nome.split()
print('Seu primeiro nom é {}. E tem {} letras.'.format(separa[0], len(separa[0])))
print('---------------'*3)

