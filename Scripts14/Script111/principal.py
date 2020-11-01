'''Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''
import moeda
#from moeda import metade, dobro, aumentar
p = ''
p = float(input(f'Digite o preço - {moeda.moeda(p)}'.center(30)))
moeda.resumo(p, 10/2, 16/2)
