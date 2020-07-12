'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = ''
sexo = str(input('Informe seu sexo: ')).strip().upper()
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()
if sexo == 'M' or sexo == 'F':
        print('Sexo {} registrado com sucesso.'.format(sexo))