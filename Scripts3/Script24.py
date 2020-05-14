''' Jonatan Paschoal 11/05/2020 - Crie um programa que receba nome de cidades e verifique se começa com a palavra Santo'''

print('---------------'*3)
cidade = input('Digite o nome de uma cidade: ')
#------------------------------------------------------------
x = cidade.split()
#-------------------------------------------------------------
a = (x[0])
#-------------------------------------------------------------
print('O nome da cidade começa com - {}.'.format(a.capitalize()))

print('---------------'*3)
# Resposta alternativa
print('Resposta alternativa')
cid = str(input('Em que cidade você nasceu? ')).strip()
VerdFalso = cid[:5].upper() == 'SANTO'
print('Verdadeiro ou falso: {}'.format(VerdFalso))
print('---------------'*3)