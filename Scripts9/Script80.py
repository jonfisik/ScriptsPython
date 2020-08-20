'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
print('-='*30)
print(f'{"LISTA ORDENADA":^60}')
print('-='*30)

lista = []
for c in range(0,10):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]: # lista[len(lista)-1] --> lista[-1]
        lista.append(n)
        print('Add no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Add na posição {pos+1} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')
print('-='*30)