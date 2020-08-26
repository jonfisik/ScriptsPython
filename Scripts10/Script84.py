'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
print('-='*20)
nomeTemp = []
princ = []
maior = menor = 0
while True:
    nomeTemp.append(str(input('Digite seu nome: ')))
    nomeTemp.append(int(input('Peso: ')))
    
    if len(princ) == 0:
        maior = menor = nomeTemp[1]
    else:
        if nomeTemp[1] > maior:
            maior = nomeTemp[1]
        if nomeTemp[1] < menor:
            menor = nomeTemp[1]
    
    princ.append(nomeTemp[:])
    nomeTemp.clear()

    opcao = str(input('Quer continuar? [S/N] '))
    print('--'*20)
    if opcao in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
print('-='*20, end='')
print()