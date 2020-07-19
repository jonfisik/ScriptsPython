'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('-=-=-=-=-=-'*3)
titulo = str('GERADOR DE PA')
print('{:^33}'.format(titulo))
print('-=-=-=-=-=-'*3)
n = int(input('Quantos termos você quer calcula? '))
prim = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('-=-=-=-=-=-'*3)
termo = prim
cont = 1
while cont <= n:
    print('{}º = {} -> '.format(cont,termo), end='')
    termo = termo + razao
    cont = cont + 1 
print('FIM')
