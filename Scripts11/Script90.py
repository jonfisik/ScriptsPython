'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
dados = dict()
condicao = list()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de "{dados["nome"]}": '))
condicao.append(dados.copy())
print('=+='*10)
print(condicao)
if dados['media'] >= 7:
        print('aprovado')
elif 5 < dados['media'] < 7:
        print('recuperação')
else:
        print('Reprovado')
