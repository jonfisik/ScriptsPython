'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e sorteando o nome do escolhido.'''
import random
print('------'*8)
print(' Digite o nome de quatro alunos para o sorteio: ')
a = input(' Aluno 1: ')
b = input(' Aluno 2: ')
c = input(' Aluno 3: ')
d = input(' Aluno 4: ')
#O método choice escolhe itens em lista.
print(' O aluno sorteado é >> {} <<!'.format(random.choice([a,b,c,d]))) 
print('------'*8)