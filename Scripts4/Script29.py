'''Jonatan Paschoal  - 15 /05 /2020. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma msn mostrando que ele foi multado. A multa vai custar R$ 7,00 por quilômetros acima do limite.'''

print('-----------------'*3)
vel = float(input('Digite o valor da velocidade registrada: '))
x = abs(vel - 80)
print('-----------------'*3)
if vel <= 80:
    print('Você está {} km/h abaixo da média de 80 km/h.'.format(x))
else:
    print('Você ultrapassou {} km/h dá media.'.format(x))
    print('Você terá que pagar R$ {:.2f}.'.format(x * 7))
print('-----------------'*3)