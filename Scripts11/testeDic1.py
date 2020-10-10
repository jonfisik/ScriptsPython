pessoas = {'nome': 'jonatan', 'sexo': 'M', 'idade': 39}
print('---'*15)
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('---'*15)

for k in pessoas.keys():
    print(k)

print('---'*15)

for v in pessoas.values():
    print(v)

print('---'*15)

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('---'*15)
del pessoas['sexo']
pessoas['nome'] = 'Augusto'
pessoas['peso'] = 85
for k, v in pessoas.items():
    print(f'{k} = {v}')