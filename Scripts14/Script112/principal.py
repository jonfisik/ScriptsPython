'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
import moeda
import dados
#from moeda import metade, dobro, aumentar
print('---'*15)
p = ''
p = dados.leiaDinheiro(f'Digite o preço - {moeda.moeda(p)}'.center(30))
moeda.resumo(p, 10/2, 16/2)
