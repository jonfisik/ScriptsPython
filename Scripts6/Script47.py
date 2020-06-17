'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('CONTAGEM PARES')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
print('\n')
for c in range(1,50,2):
    print(c+1, end=' ')
    if c > 36:
        print('\n', end=' ')
print('=+=+=+=+=+=+=+=+='*3)