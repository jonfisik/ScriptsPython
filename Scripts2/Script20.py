'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trbalhos de alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada'''
import random
print('------'*8)
a = input(' Aluno 1: ')
b = input(' Aluno 2: ')
c = input(' Aluno 3: ')
d = input(' Aluno 4: ')
e = random.randint(1,4)
f = random.randint(1,3)
g = random.randint(1,2)
h = random.randint(1,1)
print('O aluno sorteado é {},{},{},{}!'.format(e,f,g,h))
print('------'*8)