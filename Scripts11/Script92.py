'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho ("0" não tem): '))
if dados['CTPS'] != 0:
    dados['Contratacao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratacao'] + 35) - datetime.now().year)
print('-=-'*30)
if dados['CTPS'] == 0:
    for k, v in dados.items():
        print(f'  - {k}: {v}.')
    print('Não posssui carteira de')
else:
    for k, v in dados.items():
        print(f'  - {k}: {v}.')