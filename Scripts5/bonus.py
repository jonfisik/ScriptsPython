from time import sleep
print('=+=+=+=+=+=+=+=+='*3)
print('Olá, vamos conversar?')
nome = str(input('Digite seu nome: ')).strip()
nome = nome.lower()
if 'jonatan' in nome:
    print('uhm...')
    print('Esse nome é muito lindo!!! Apaixonei')
else:
    print('Uhm, {} que nome mais comum.'.format(nome.capitalize()))
#-----------------------------------------------------
if nome == 'jonatan':
    idade = int(input('Bonitão, qual tua idade? '))
    print('{}? Só isso? Sempre Jovem!'.format(idade))
else:
    print('Pesando...')
    print('E tua idade?')
    sleep(3)
    print('Tá com pressa?')
    sleep(4)
    idade = int(input('Fala a verdade! '))
    if idade <= 25:
        print('Criança.')
    else:
        print('Tá maduro(a) heim!!')
         
print('fim')

print('=+=+=+=+=+=+=+=+='*3)