'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo'''
while True:
    print('- -'*15)
    tab = int(input('Quer ver a tabuada de quanto? '))
    if tab < 0:
        break
    print('- -'*15)
    for cont1 in range(1, 11):
        prod = tab * cont1
        print(f'{tab} x {cont1} = {prod}.')
print('- -'*15)
print('TABUADA ENCERRADA - Volte sempre!!!')
print('- -'*15)

    

