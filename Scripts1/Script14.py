'''Escreva um program que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por quilômetro rodado.'''
print('===='*9)
dias = float(input('Quantos dias alugados? '))
quilometro = float(input('Quantos km rodado? '))
total = (dias * 60) + (quilometro * 0.15)
print('O total a ser pago é R$ {:.2f}.'.format(total))
print('===='*9)