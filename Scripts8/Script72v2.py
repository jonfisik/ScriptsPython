'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
#----------------------------------------------------
tupla20 = ('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
print('-'*40)
while True:
    numero = int(input('Digite um número entre 0  e 20. >>> '))

    if 0 <= numero <=20:
        print(f'Você digitou o número "{tupla20[numero]}".')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-'*40)
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break

    else:
        print('Tente novamente. ', end = '')

print('Saindo do programa...')    
    

