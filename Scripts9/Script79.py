'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
print('-='*30)
print(f'{"LISTAS":^60}')
print('-='*30)
#----------------------------------------
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor add com sucesso!')
        print('--'*30)
    else:
        print('Valor duplicado! Não será adicionado...')
        print('--'*30)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('--'*30)
num.sort()
print(f'Você digitou os valores {num}.')
print('-='*30)