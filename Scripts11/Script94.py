'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
#-----------------------------------------------------
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    while True:
        x = input('Idade: ')
        if x.isnumeric():
            pessoa['idade'] = int(x)
            break
        print('ERRO! Por favor, digite apenas valores inteiro.')
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta= str(input('Quer continuar? [S/N] ')).strip().upper()
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=-'*15)
print(f'A) Foram cadastradas {len(galera)} pessoas.')
media = soma/len(galera)
print(f'B) A média das idades é {media:5.2f} anos.')
print('C As mulheres cadastradas foram ', end='')#end - não quebrar de linha
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista das pessoas assima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('         ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print(f'{"<<< ENCERRADO >>>":^45}')