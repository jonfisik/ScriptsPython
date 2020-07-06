'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('TERMOS DE UMA P.A.')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
TermoUm = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
numero = int(input("Digite o número de termos: "))
print('-----------------'*3)
#-----------------------------------------------------
TermoFinal = TermoUm + (numero-1)*razao
for c in range(TermoUm,TermoFinal+razao,razao):
    print('{} '.format(c), end='- ')
print('ACABOU!')
print('-----------------'*3)