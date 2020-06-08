'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule se IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso - Entre 18.5 e 25: peso ideal - 25 até 30: sobrepeso - 30 até 40: obesidade - Acima de 40: Obesidade mórbida.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('Teste IMC')
print('{:^51}'.format(titulo))
print('-----------------'*3)
massa = float(input('Digite sua massa em [kg]: '))
altura = float(input('Digite sua altura em [m]: '))
print('-----------------'*3)
IMC = (massa/(altura * altura))
#-------------------------------------------------
print('Seu IMC é {:.1f}.'.format(IMC))
if  IMC < 18.5:
    print('Classificação - abaixo do peso.')
elif IMC >= 18.5 and IMC < 25:
    print('Classificação - peso ideal.')
elif IMC >= 25 and IMC < 30:
    print('Classificação - sobrepeso.')
elif IMC >= 30 and IMC <= 40:
    print('Classificação - obesidade.')
elif IMC > 40:
    print('Classificação - obesidade mórbida.')
print('=+=+=+=+=+=+=+=+='*3)