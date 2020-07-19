'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('-=-=-=-=-=-'*3)
titulo = str('SUPER GERADOR DE PA')
print('{:^33}'.format(titulo))
print('-=-=-=-=-=-'*3)
n = int(input('Quantos termos você quer calcula? '))
prim = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('-=-=-=-=-=-'*3)
termo = prim
cont = 1
termosMais = 1
while termosMais != 0:
    n = n + termosMais
    while cont <= n - 1:
        print('[{}º] = {}; '.format(cont,termo), end='')
        termo = termo + razao
        cont = cont + 1 
    print(' PAUSA...')
    termosMais = int(input('Quantos termos quer mostrar a mais? '))
print('-----------'*3)
print('PA finalizada com {} termos mostrados.'.format(n-1))
print('-=-=-=-=-=-'*3)
