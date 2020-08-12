'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''
#
times = ('Athletico-PR','Sport','Atlético-MG','Grêmio','Inter','Santos','Bragantino','Atlético-GO',
        'Bahia','Botafogo','Corinthians','Goiás','Palmeiras','São Paulo','Vasco','Ceará','Coritiba','Flamengo','Fluminense','Fortaleza')
print('-='*70)
print(f'Rank dos 20 primeiros times - {times}')
print('-='*70)
for t in times:
    print(f' - {t} ', end ='')
print('-='*70)
print(f'Ranck 5 primeiros - {times[0:5]}')
print('-='*70)
print(f'Os 4 últimos - {times[16:20]}')
print('-='*70)
print(f'Times em ordem alfabética - {sorted(times)}')
print('-='*70)
c =times.index('Inter')
print(f'O {times[c]} está na {c}ª posição.')
print('-='*70)
