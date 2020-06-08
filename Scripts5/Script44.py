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
pag = int(input('Qual é a opção? '))
parc = int(input('Quantas parcelas? '))
#-------------------------------------------------
if pag !=1 and pag !=2 and pag !=3 and pag !=4:
    nPreco = 0
    print('Opção ERRADA!')
    if pag == 1:
        nPreco = valor - (valor * 0.1)
        print('Sua comprar será paga à vista.')
    elif pag == 2:
        nPreco = valor - (valor * 0.05)
        print('Sua compra será paga à vista com acréscimo de R$ {}.'.format(valor * 0.05))
    elif pag == 3:
        nPreco = valor
        print('Sua compra será parcelada em 2x de {} sem juros.'.format(nPreco/2))
    elif pag == 4:
        nPreco = valor + (valor * 0.2)
        print('Sua compra será parcelada em {}x de {} sem juros.'.format(parc, nPreco/parc))
    print('Valor de compra R${}. Valor total compra R${}.'.format(valor,nPreco))
print('=+=+=+=+=+=+=+=+='*3)