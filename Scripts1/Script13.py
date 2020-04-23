'''Faça um programa que calcule o novo salário de um funcionário com aumento de 15%. 23/04/2020'''
print('=+='*12)
Sal = float(input('Informe o valor do salário R$ '))
Porcentagem = Sal * 0.15
NovoSal = Sal + Porcentagem
print('Seu novo salário é R$ {:.3f}.'.format(NovoSal))
print('=+='*12)