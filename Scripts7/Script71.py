####
# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao 
#  usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão 
#  entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
####
print('='*40)
titulo = 'BANCO JA'
print(f'{titulo:^40}')
print('='*40)
#------------------------------------
valores = 'Notas de R$ 50, R$ 20, R$ 10 e R$ 1.'
print(f'{valores:^40}')
print('-'*40)
saque = int(input('Que valor você quer sacar? R$ '))
total = saque
cedulaValor = 50
totalCedula = 0
while True:
    if total >= cedulaValor:
        total -= cedulaValor
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédula de R$ {cedulaValor}.')
        if cedulaValor == 50:
            cedulaValor = 20
        elif cedulaValor == 20:
            cedulaValor = 10
        elif cedulaValor == 10:
            cedulaValor = 1
        totalCedula = 0
        if total == 0:
            break
print('-'*40)
print('{:^40}'.format('Volte sempre ao BANCO JA.'))
print('='*40)