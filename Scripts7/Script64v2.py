'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). 23/07/2020 jonatan paschoal'''
num = contador = somador = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    somador += num #somador = somador + num
    contador += 1 #contador = contador + 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles é {}.'.format(contador, somador))
print('FIM')