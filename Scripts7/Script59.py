'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
print('-----'*6)
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
print('-----'*6)
opcao = 0
while opcao != 5:
    print('''         [ 1 ] somar
         [ 2 ] multiplicar
         [ 3 ] maior
         [ 4 ] novos números
         [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção: '))
    print('-----'*6)
    if opcao == 1:
        print('A soma de {} e {} é {}.'.format(val1,val2,val1+val2))
    elif opcao == 2:
        print('O produto de {} e {} é {}.'.format(val1,val2,val1*val2))
    elif opcao == 3:
        if val1 > val2:
            print('{} é maior que {}.'.format(val1,val2))
        else:
            print('{} é menor que {}.'.format(val1,val2))
    elif opcao == 4:
        val1 = int(input('Digite novamente o primeiro valor: '))
        val2 = int(input('Digite novamente o segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa...')
        sleep(2)
        print('Obrigado. Volte sempre!')
    else:
        print('Opção inválida. Tente Novamente!')
    print('-----'*6)
    
    