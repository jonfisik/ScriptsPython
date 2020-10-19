'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(*num): #* receber vários parâmetros e desenpacotar
    print('-=-=-'*5)
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    if maior == 0:
        print(f'Não foi informado nenhum valor.')
    else:
        print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2,3,1,6,5,7,9)
maior(6,3,5,10,6,9,7,11)
maior(1,3,5,9)
maior(9,8)
maior()
