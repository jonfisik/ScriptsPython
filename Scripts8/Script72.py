'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
#----------------------------------------------------
tupla20 = ('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print('-'*40)
numero = int(input('Digite um número entre "0" e "20" >>> '))
while numero not in range(0,21):
    numero = int(input('ERRO. Digite novamente. Nº entre "0" e "20" >>> '))

print(f'Você digitou o número "{tupla20[numero]}".')
print('-'*40)

