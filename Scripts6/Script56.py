'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
print('-=-=-=-=-=-'*4)
titulo = str('ANALISADOR COMPLETO')
print('{:^44}'.format(titulo))
print('-=-=-=-=-=-'*4)
#---------------------------------------------------
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
#---------------------------------------------------
for c in range(1,5):
    subtitulo = str('------ {}ª pessoa ------'.format(c))
    print('{:^44}'.format(subtitulo))
    nome = str(input('  Nome: ')).strip()
    idade = int(input('  Idade: '))
    sexo = str(input('  Sexo: [M/F]: '))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

    print('-----------'*4)
mediaidade = somaidade / 4
print('A média de idade do grupo é de {}.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('O total de mulher com idade menor de 20 anos é {}.'.format(totmulher))
print('-----------'*4)