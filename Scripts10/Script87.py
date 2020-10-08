'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
somaPar = maior = somaCol = 0
print('-+-'*15)
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para ({linha},{coluna}): '))
print('-+-'*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()
for linha in range(0,3):
    somaCol += matriz[linha][2]
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print('-+-'*15)
print(f'soma dos valores pares: {somaPar}.')
print(f'Soma dos elementos da coluna 3: {somaCol}')
print(f'Maior elemento da linha 2: {maior}.')
print('-+-'*15)

