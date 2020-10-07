'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
numero = [[],[]]
print('-+-'*15)
valorProv = 0
for c in range(1,8):
    valorProv = int(input(f'Digite o {c}o. valor: '))
    if valorProv % 2 == 0:
        numero[0].append(valorProv)
    else:
        numero[1].append(valorProv)
print('-+-'*15)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')
print('-+-'*15)
