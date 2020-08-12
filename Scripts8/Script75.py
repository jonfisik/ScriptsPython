'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
print('-'*40)
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('-'*40)
print(f'Você digitou os valores: {num}.')
print('-'*40)
print(f'Você digitou {num.count(9)} vez(es) o número 9.')
print(f'O número 3 está na {num.index(3)+1}ª posição.')
print('Os números pares foram: ',end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
print('\n')
print('-'*40)