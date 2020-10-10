brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado1)
print(brasil)
print(brasil[1])

print(brasil[0])


print(brasil[1]['UF'])
print(brasil[1]['sigla'])
print('---'*15)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
print('---'*15)
for e in brasil:
    print(e)
print('---'*15)
for e in brasil: # for da lista
    for k, v in e.items(): #for do dicionario
        print(f'O Campo {k} tem valor {v}.')
print('---'*15)
for e in brasil: # for da lista
    for v in e.values(): #for do dicionario
        print(v, end='')
    print()