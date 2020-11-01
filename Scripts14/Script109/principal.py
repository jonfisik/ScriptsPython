'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''
import moeda3
#from moeda import metade, dobro, aumentar
p = ''
print('-=-'*15)
p = float(input(f'Digite o preço - {moeda3.moeda(p)}'))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, True)}.')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, True)}.')
print(f'Aumentando 10%, temos {moeda3.aumentar(p, 10, True)}.')
print(f'Diminuindo 10%, temos {moeda3.diminuir(p, 23, True)}.')
print('-=-'*15)