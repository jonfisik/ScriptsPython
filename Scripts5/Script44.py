'''Elabore um programa que calcule o valr a ser pago por um porduto, considerando o seu preço normal e condição de pagamento: 
- à vista dinheiro/cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('LOJA BARATEIRA')
print('{:^51}'.format(titulo))
print('-----------------'*3)
valor = float(input('QUal o valor da comprar? R$ '))
print('-----------------'*3)
print('Formas de PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print('-----------------'*3)
pag = float(input('Qual é a opção? '))
parc = float(input('Quantas parcelas? '))
#-------------------------------------------------
if pag == 1:
    print('Sua comprar será paga à vista.')
    print('Valor da compra R$ {}.'.format(valor))
elif pag == 2:
    nPreco = valor + (valor * 0.05)
    print('Sua compra será paga à vista com acréscimo de R$ {}.'.format(valor * 0.05))
    print('Valor total compra R$ {}.'.format(nPreco))
elif pag == 3:
    print('Sua compra será parcelada em {}x de {} sem juros.'.format(parc, nPreco/parc))
    print('Valor total compra R$ {}.'.format(valor))
elif pag == 4:
    print('Sua compra será parcelada em {}x de {} sem juros.'.format(parc, nPreco/parc))
    print('Valor total compra R$ {}.'.format(nPreco))
print('=+=+=+=+=+=+=+=+='*3)