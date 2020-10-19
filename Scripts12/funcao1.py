# funções
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

def linha():
    print('---'*15)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos - {s}.')


# programa principal
linha()
a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))

soma(a, b)
print(soma)

linha()
contador(3,1,6)
contador(1001,2002,5623,3210)
contador(1,3,5,9,4,2,7)

linha()
valores = [3,2,6,5,1,0,8,9,7]
print(valores)
dobra(valores)
print(valores)

linha()
soma2(2,3,6)
soma2(2,3)

linha()