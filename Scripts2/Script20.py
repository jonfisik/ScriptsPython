'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trbalhos de alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada'''
import random
print('-------'*8)
print(' Digite o nome de quatro alunos para o sorteio: ')
a = str(input(' Aluno 1: '))
b = str(input(' Aluno 2: '))
c = str(input(' Aluno 3: '))
d = str(input(' Aluno 4: '))
lista = [a,b,c,d]
random.shuffle(lista) # O método shuffle embaralha a sequencia de uma lista.
print(' A ordem do sorteio é {}!'.format(lista))
print('-------'*8)