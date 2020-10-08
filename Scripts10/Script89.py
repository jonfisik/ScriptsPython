'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
ficha = list()
print('---'*15)
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2

    ficha.append([nome,[nota1,nota2],media])

    resposta = str(input('Quer continuar? [S/N]: '))
    print('---'*15)
    if resposta not in 'SsNn':
        print('Atenção, responda [S/N]!')
        resposta = str(input('Quer continuar? [S/N]: '))
    print('---'*15)
    if resposta in 'Nn':
            break
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":<10}')
print('---'*15)
for indice, a in enumerate(ficha):
    print(f'{indice:<5}{a[0]:<15}{a[2]:<10.1f}')
print('---'*15)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999, para interromper). '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('<<<   VOLTE SEMPRE   >>>')