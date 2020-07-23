'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
resp = 'S'
contador = somador  = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    somador += num
    contador += 1
    if contador == 1:
        maior = menor  = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
#-------------------------------- 
media = somador/contador
print('Você digitou {} números e sua média foi {}.'.format(contador, media))
print('O maior número é {} e o menor {}.'.format(maior,menor))
