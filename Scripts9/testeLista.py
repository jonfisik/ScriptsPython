print('-'*10)
num = [2,5,9,11]
num[2] = 3
num.append(8)
num.sort(reverse=True)
num.insert(1,8)
if 10 in num:
    num.remove(10)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa leitura tem {len(num)} elementos.')
print('-'*10)
lista1 = [] # lista vazia
lista2 = list() # lista vazia

lista1.append(5)
lista1.append(9)
lista1.append(4)

for l in lista1:
    print(f'{l}...')
print('\n')
for l in lista1:
    print(f'{l}...', end = '')

print('\n')
print('-'*10)

for chave, l in enumerate(lista1):
    print(f'Na posição {chave} encontrei o valor {l} !')
print('Cheguei ao  final da lista.')
print('-'*10)

for cont in range(0,5):
    lista2.append(int(input('Digite um valor: ')))

for chave, l in enumerate(lista2):
    print(f'Na posição {chave + 1} encontrei o valor {l}.')
print(lista2)
print('Outro fim!!!')

print('-'*10)

a = [3,2,6,9,1,0,8]
b = a
print(f'Lista A = {a}')
print(f'Lista B = {b}')
b[1] = -9
print('-'*10)
print('Lista A conectada com B')
print(f'Lista A = {a}.') # ligação entre lista
print(f'Lista B = {b}')
print('-'*10)
print('Lista B é cópia de A.')
b = a[:] # lista B é cópia e A
b[1] = 100
print(f'Lista A = {a}')
print(f'Lista B = {b}')