'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
print('=+=+=+=+=+=+=+=+='*3)
titulo = 'CATEGORIA'
print('{:^51}'.format(titulo))
print('-----------------'*3)
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
 
cat = atual - nasc
print('-----------------'*3)
if cat <= 9:
    print('Com {} anos sua categoria é MIRIM.'.format(cat))
elif cat > 9 and cat <= 14:
    print('Com {} sua categoria é INFANTIL.'.format(cat))
elif cat > 14 and cat <= 19:
    print('Com {} anos sua categoria é JUNIOR.'.format(cat))
elif cat > 19 and cat <=25:
    print('Com {} anos sua categoria é SÊNIOR'.format(cat))
elif cat > 25:  
    print('Com {} anos sua categoria é MASTER'.format(cat))
print('=+=+=+=+=+=+=+=+='*3)