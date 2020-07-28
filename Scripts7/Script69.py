'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:'''
print('----'*8)
titulo = 'CADASTRO PESSOA'
print(f'{titulo:^30}')
contadorFem = contadorMasc = contadorMaior = contadorMaiorVinte = 0
opcao = ' '
while opcao not in 'N':
    print('----'*8)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    print('----'*8)
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    #if opcao not in 'FM':
        #print('Digite CORRETAMENTE, por favor.')
    if sexo == 'M':
        contadorMasc += 1
    else:
        contadorFem += 1
        if idade <= 20:
            contadorMaiorVinte += 1
    if idade >= 18:
        contadorMaior += 1
print('----'*8)
print('A todo temos:  ')
print(f'- {contadorMaior} maior(es) de 18 anos.')
print(f'- {contadorMasc} homem(ns) cadastrado.')
print(f'- {contadorMaiorVinte} mulher(es) maiores de 20 anos.')
print('----'*8)
#print(contadorFem,contadorMasc,contadorMaior)