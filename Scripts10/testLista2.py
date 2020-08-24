print('--'*30)
nomeIdade = list()
nomeIdade.append('Jonatan')
nomeIdade.append(39)
galera = list()
galera.append(nomeIdade[:])
nomeIdade[0] = 'Amanda'
nomeIdade[1] = 36
galera.append(nomeIdade[:])
print(galera)
print('--'*30)
#-----------------------------------------------------
galera2 = [['Jonatan',17],['Gabriel',16],['Isaac',10]]
print(f'1 - {galera2}')
print(f'2 - {galera2[0][0]}')
print(f'3 - {galera2[1][0]}')
print(f'4 - {galera2[2][1]}')
print(f'5 - {galera2[2]}')
print('--'*30)
#-----------------------------------------------------
for pessoa in galera2:
    print(pessoa)
print('--'*30)
for pessoa in galera2:
    print(pessoa[0])
print('--'*30)
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
print('--'*30)
#-----------------------------------------------------
# receber elementos na lista
galera3 = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear() #apaga dados a cada volta(loop)
print(galera3)

totmaior = totmenor = 0
for pessoa in galera3:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')
print('--'*30)
