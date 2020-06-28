'Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. 28/06/2020.'
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('TABUADA')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
num = int(input('Digite um número: '))
num2 = int(input('Até quanto você quer calcular? '))
for c in range(1,num2+1):
    if c < num2+1:
        resp = num * c
    print('{} x {} = {}'.format(num,c,resp)) 