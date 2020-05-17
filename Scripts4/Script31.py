'''Desenvolva um progama que descreva a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ por km 0,50 para viagens de 200 km e R$ 0,45 para viagens mais longas.'''
print('---------------'*3)
dist = float(input('Qual a distância em km de sua viagem: '))
traco = ('---------------------')
print('{:^45}'.format(traco))
if dist >= 200:
    print('Para {} km sua passagem custará R$ {:.2f}'.format(dist, dist * 0.5))
else:
    print('Para {} km sua passagem custará R$ {:.2f}'.format(dist, dist * 0.45))
print('{:^45}'.format(traco))
fim = ('Boa viagem!')
print('{:^45}'.format(fim))
print('---------------'*3)