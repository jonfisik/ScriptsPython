'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome da pessoa.'''
print('--------'*5)
n = str(input("Digite seu nome: ")).strip()
nome = n.split()
print(len(nome))
print('Prazer em te conhecer.')
print('Seu primeiro nome é - {}.'.format(nome[0]))
print('Seu último nome é - {}.'.format(nome[len(nome) - 1]))
print('--------'*5)