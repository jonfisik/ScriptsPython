'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('programação','computação','ciência','física','matemática','estudar','jonatan','casamento','rio')
print('-'*40)
for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos - ', end = '')
    for letra in p:
        if letra.lower() in 'aeiouàáéèíìóòúùâêîôûãõ':
            print(letra, end = ' ')
print('\n')
print('-'*40)