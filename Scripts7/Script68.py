'''while - repetição com teste lógico.'''
resp = 'S'
while resp == 'S':
    numero = int(input('Digite um valor inteiro: '))
    resp = str(input('Quer continuar [S/N]: ')).upper()
print('Fim.')
