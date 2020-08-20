'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
print('=-'*30)
listanum = []
maior = menor = 0
for i in range(0,5):
    listanum.append(int(input(f'Digite um valor: para posição {i}: ')))
    if i == 0:
        maior = menor = listanum[i]
    else:
        if listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]
print('=-'*30)
print(f'Você digitou os valores lista = {listanum}.')
print(f'O maior valor digitado foi {maior}, na(s) posição(ões): ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado é {menor}, na posição(ões): ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
print('=-'*30)