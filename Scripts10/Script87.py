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
print('-+-'*15)
print(f'A soma dos valores par é: {somaPar}.')
print('-+-'*15)

