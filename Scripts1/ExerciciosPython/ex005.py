'''Faça um programa que receba a temperatura em graus celsius e transforme para as escalas Farnheit e Kelvin.'''
print('====='*10)
c = float(input('Digite um valor de temperatura em Celsius: '))
f = (9 / 5) * c + 32
k = c + 237
print('Temos {:.1f}°F e {:.1f}K'.format(f,k))
print('====='*10)