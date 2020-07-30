'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('-'*50)
titulo = 'LOJA BARATÃO'
print(f'{titulo:^50}')
print('-'*50)
Total = PrecoMaior = PrecoMenor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$ '))
    cont += 1
    Total += preco
    #--------------------------
    if preco > 1000:
        PrecoMaior += 1
    #--------------------------
    if cont == 1:
        PrecoMenor = preco
        barato = produto
    else:
        if preco < PrecoMenor:
            PrecoMenor = preco
            barato = produto
    #--------------------------
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
    print('{:^50}'.format('------------------------------'))

print('{:-^50}'.format('RESUMO DA COMPRA'))
print(f'O total da compra foi R$ {Total:.2f}')
print(f'Temos {PrecoMaior} produtos com mais de R$ 1000.00.')
print(f'O produto mais barato foi {barato} e custa R$ {PrecoMenor}')
print('-'*50)

