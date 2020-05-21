'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('=+=+=+=+=+=+=+=+='*3)
nome = str(input('Digite seu nome: ')).strip()
sal = float(input('Informe sua renda mensal: R$ '))
preco = float(input('Qual o valor da casa? R$ '))
tempo = int(input('Em quanto anos você deseja parcelar sua conta? '))
print('-----------------'*3)
meses = tempo * 12
parcela = preco/(meses)

if parcela >= (sal * 0.3) and tempo <=15:
    print('{}, não será possível a compra da casa.'.format(nome))
    print('A parcela de R$ {:.2f} execede 30% dos seus rendimento.'.format(parcela))
else:
    print('Parabéns, você foi aprovado.')
    print('Sua parcela é de R$ {:.2f}. Distribuidos em {} meses.'.format(parcela,meses))
print('=+=+=+=+=+=+=+=+='*3)