from time import sleep
from datetime import date
print('=+=+=+=+=+=+=+=+='*3)
print('Olá, vamos conversar?')
sleep(2)
nome = str(input('Diga seu nome: ')).strip()
nome = nome.lower()

if 'jonatan' in nome:
    print('uhm...')
    print('Esse nome é muito lindo!!! Apaixonei')
else:
    print('Uhm, {} que nome mais comum.'.format(nome.capitalize()))
#-----------------------------------------------------
if nome == 'jonatan':
    idade = int(input('Bonitão, qual tua idade ess ano? '))
    print('{}? Só isso? Sempre Jovem!'.format(idade))
else:
    print('Pesando...')
    print('E quantos anos você fez ou faz esse ano? ')
    sleep(6)
    print('Tá com pressa?')
    idade = int(input('Fala a verdade! '))
    if idade <= 25:
        print('Criança.')
    else:
        print('Tá maduro(a) heim!!')
anoAtual = date.today().year
ano = anoAtual - idade
#----------------------------------------------------
if ano > 2000:
    print('{} é do novo século, menos mal!'.format(ano))
elif ano < 2000 and ano != 1981:
    print('{} velha guarda. Século passado.'.format(ano))
elif ano == 1981:
    print('{}! A safra foi boa!!'.format(ano))
print('A gente conversa mais depois.')
         
print('fim')

print('=+=+=+=+=+=+=+=+='*3)