'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Transferidor',4.2,
            'Compasso',9.99,
            'Mochila',120.0)
print('-'*40)
print(f'{"LISTAGEM PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*40)
print(f'{"FIM LISTA":^40}')
print('-'*40)
