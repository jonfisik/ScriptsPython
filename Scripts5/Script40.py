'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = 'MÉDIA'
print('{:^51}'.format(titulo))
print('-----------------'*3)
nota1 = float(input('Digite nota 1: '))
nota2 = float(input('Digite nota 2: '))

media = float((nota1+nota2)/2)
rec = (12 - media)
print('-----------------'*3)
if media >= 7:
    print('Aprovado com média {:.1f}.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Recuperação com média {:.1f}.'.format(media))
    print('Você precisa alcança nota {:.1f} na recuperação.'.format(rec))
elif media < 5:
    print('Reprovado. Média {}.'.format(media))
print('=+=+=+=+=+=+=+=+='*3)