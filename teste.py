'''teste while - break'''
print('--'*20)
n = c = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    c += 1
print('--'*20)
print('A soma vale {} dos {} números digitados.'.format(s,c))
print(f'A soma vale {s} dos {c} números digitados.') #fstring (f'{variável:.2f}')
print('--'*20)